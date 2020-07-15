import json
from typing import List, Dict

from DataI import enums
from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.Filters.FiltersController import FiltersController
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
    def getFinalTables(cls, data: DataModel) -> List[TableModel]:
        # Aggregation should be added here.
        return cls.__getFilteredTables(data)

    @classmethod
    def __getFilteredTables(cls, data: DataModel) -> List[TableModel]:
        tables = list()
        for table in data.dataSources:
            tables.append(FiltersController.getFilteredTable(data, table.id))
        return tables

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
    def getRowFromTable(cls, table: TableModel, rowIndex: int) -> List[CellModel]:
        row = list()
        for column in table.columns:
            row.append(column.cells[rowIndex])
        return row

    @classmethod
    def updateRowInTable(cls, table: TableModel, rowIndex: int, row: List[CellModel]):
        for column, i in zip(table.columns, range(len(table.columns))):
            column.cells[rowIndex].value = row[i].value
            column.cells[rowIndex].type = row[i].type

    @classmethod
    def removeRowFromTable(cls, table: TableModel, rowIndex: int):
        for column in table.columns:
            column.cells.pop(rowIndex)

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
    def cellInList(self, cell, list):
        for item in list:
            if item.value == cell.value:
                return True
        return False


# was duplicated here to avoid circular import
def removeRowFromTable(table: TableModel, rowIndex: int):
    for column in table.columns:
        column.cells.pop(rowIndex)

def updateCategorizedValues(column: ColumnModel):
    column.valueCategories.clear()
    for cell in column.cells[1:]:
        if not DataSourcesController.cellInList(cell, column.valueCategories):
            column.valueCategories.append(cell)
##############################################

#util functions.
def addTwoCellsLists(firstList: List[CellModel], secondList: List[CellModel]) -> List[CellModel]:
    resultList = list()
    for cell1, cell2 in zip(firstList, secondList):
        resultList.append(CellModel(cell1.value + cell2.value, cell1.type))
    return resultList



