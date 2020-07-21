from copy import deepcopy
from typing import List

from DataI import enums
from DataI.Controllers.Aggregation import Aggregation
from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.DataControllers.RowUtils import RowUtils
from DataI.Controllers.Filters import FiltersController
from DataI.Models.ColumnModel import ColumnModel, CellModel
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel


class DataSourcesController():
    @classmethod
    def insertNewTable(cls, data: DataModel, table: TableModel):
        id = DataController.getMaxIdInList(data.dataSources)
        table.id = id + 1
        data.dataSources.append(table)

    @classmethod
    def insertNewColumn(cls, data: DataModel, tableId: int, column: ColumnModel) -> TableModel:
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        data.dataSources[targetTableIndex].columns.append(column)
        return data.dataSources[targetTableIndex]

    @classmethod
    def removeColumn(cls, data: DataModel, tableId: int, columnId: int) -> TableModel:
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        targetColumnIndex = DataController.getElementIndexById(data.dataSources[targetTableIndex].columns, columnId)
        data.dataSources[targetTableIndex].columns.pop(targetColumnIndex)
        return data.dataSources[targetTableIndex]

    @classmethod
    def getFilteredTables(cls, data: DataModel) -> List[TableModel]:
        tables = list()
        for table in data.dataSources:
            tables.append(FiltersController.getFilteredTable(data, table.id))
        return tables

    @classmethod
    def getAggregatedTable(cls, data: DataModel, tableId: int, aggColumnId: int, type: str) -> TableModel:
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        targetTable = data.dataSources[targetTableIndex]
        aggregator = Aggregation.getAggregator(type)
        Aggregation.clearAggregationTable(targetTable)
        aggregator.implementAggregation(data, targetTable, aggColumnId)
        returnTable = cls.sugreCoatAggregatedTable(deepcopy(targetTable))
        returnTable.aggregator.type = type
        return returnTable

    @classmethod
    def setAggregationOn(cls, data: DataModel, tableId: int) -> TableModel:
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        targetTable = data.dataSources[targetTableIndex]
        Aggregation.setAggregationOn(targetTable)
        return targetTable

    @classmethod
    def setAggregationOff(cls, data: DataModel, tableId: int) -> TableModel:
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        targetTable = data.dataSources[targetTableIndex]
        Aggregation.setAggregationOff(targetTable)
        return targetTable

    @classmethod
    def updateTableById(cls, data: DataModel, table: TableModel, id: int):
        oldTableIndex = DataController.getElementIndexById(data.dataSources, id)
        data.dataSources[oldTableIndex] = table
        return data.dataSources[oldTableIndex]

    @classmethod
    def deleteTable(cls, data: DataModel, id: int):
        elementIndex = DataController.getElementById(data.dataSources, id)
        if elementIndex != -1:
            data.dataSources[elementIndex].isDeleted = True
            return data.dataSources[elementIndex]
        return None

    @classmethod
    def updateCellByCords(cls, data: DataModel, cell, tableId: int, columnId: int, cellIndex):
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        targetColumnIndex = DataController.getElementIndexById(data.dataSources[targetTableIndex].columns, columnId)
        data.dataSources[targetTableIndex].columns[targetColumnIndex].cells[cellIndex].value = cell
        data.dataSources[targetTableIndex].columns[targetColumnIndex].cells[cellIndex].type = cls.__getCellType(cell)
        # check if the edited cell is a title cell (the first cell is the column name).
        if cellIndex == 0:
            data.dataSources[targetTableIndex].columns[targetColumnIndex].name = str(cell)

        cls.__updateCategorizedValues(data.dataSources[targetTableIndex].columns[targetColumnIndex])

        return data.dataSources[targetTableIndex].columns[targetColumnIndex].cells[cellIndex]

    @classmethod
    def updateColumnColorById(cls, data: DataModel, color: str, tableId: int, columnId: int):
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        targetColumnIndex = DataController.getElementIndexById(data.dataSources[targetTableIndex].columns, columnId)
        data.dataSources[targetTableIndex].columnsColors[targetColumnIndex] = color
        return data.dataSources[targetTableIndex]

    @classmethod
    def updateRowColorById(cls, data: DataModel, color: str, tableId: int, rowId: int):
        targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        data.dataSources[targetTableIndex].rowsColors[rowId] = color
        return data.dataSources[targetTableIndex]

    @classmethod
    def addTwoCellsLists(cls, firstList: List[CellModel], secondList: List[CellModel]) -> List[CellModel]:
        return RowUtils.addTwoCellsLists(firstList, secondList)

    @classmethod
    def getRowFromTable(cls, columns: List[ColumnModel], rowIndex: int) -> List[CellModel]:
        return RowUtils.getRowFromTable(columns, rowIndex)

    @classmethod
    def updateRowInTable(cls, columns: List[ColumnModel], rowIndex: int, row: List[CellModel]):
        RowUtils.updateRowInTable(columns, rowIndex, row)

    @classmethod
    def removeRowFromTable(cls, columns: List[ColumnModel], rowIndex: int):
        RowUtils.removeRowFromTable(columns, rowIndex)

    @classmethod
    def __getCellType(cls, cell):
        isDigit = str(cell).replace('.', '').isdigit()
        if isDigit:
            return enums.CellType.numeric.value
        else:
            return enums.CellType.string.value

    @classmethod
    def __updateCategorizedValues(cls, column: ColumnModel):
        column.valueCategories.clear()
        for cell in column.cells[1:]:
            if not cls.cellInList(cell, column.valueCategories):
                column.valueCategories.append(cell)


    @classmethod
    def sugreCoatAggregatedTable(cls, table: TableModel) -> TableModel:
        if table.aggregator.isActive:
            table.columns.clear()
            table.columns.extend(table.aggregator.aggregatedTable)
            table.rowsColors = table.rowsColors[:len(table.aggregator.aggregatedTable[0].cells) - 1]
            table.rowsVisibility = table.rowsVisibility[:len(table.aggregator.aggregatedTable[0].cells) - 1]
            return table
        else:
            return table


    @classmethod
    def cellInList(self, cell, list):
        for item in list:
            if item.value == cell.value:
                return True
        return False


# was duplicated here to avoid circular import

def getRowFromTable(columns: List[ColumnModel], rowIndex: int) -> List[CellModel]:
    return DataSourcesController.getRowFromTable(columns, rowIndex)


def updateRowInTable(columns: List[ColumnModel], rowIndex: int, row: List[CellModel]):
    DataSourcesController.updateRowInTable(columns, rowIndex, row)


def removeRowFromTable(columns: List[ColumnModel], rowIndex: int):
    DataSourcesController.removeRowFromTable(columns, rowIndex)


# ============================================================

def updateCategorizedValues(column: ColumnModel):
    column.valueCategories.clear()
    for cell in column.cells[1:]:
        if not DataSourcesController.cellInList(cell, column.valueCategories):
            column.valueCategories.append(cell)


##############################################

# util functions.

def addTwoCellsLists(firstList: List[CellModel], secondList: List[CellModel]) -> List[CellModel]:
    return DataSourcesController.addTwoCellsLists(firstList, secondList)
