from copy import deepcopy
from typing import List

from dateutil.parser import parse

from DataI import enums
from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.DataControllers.RowUtils import RowUtils
from DataI.Controllers.Filters import FiltersController
from DataI.Models.ColumnModel import CellModel, ColumnModel
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel


class BasicSumAggregation():

    def __init__(self):
        self.compareUtil = basicCompare

    def implementAggregation(self, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        filteredTable = filterAgent(data, 0, modelId)
        cols = self.aggregateTable(filteredTable, aggregationBaseColumnId)
        return cols

    def aggregateTable(self, table: TableModel, aggregationBaseColumnId: int) -> List[ColumnModel]:
        aggregatedBufferColumns = list()

        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        table.columns[aggregationColumnIndex].valueCategories = \
            deepcopy(table.columns[aggregationColumnIndex].valueCategories)

        self.__initAggregatedBufferColumns(aggregatedBufferColumns, aggregationBaseColumnId,
                                           deepcopy(table.columns))

        for categorizedValue, aggRowIndex in zip(table.columns[aggregationColumnIndex].valueCategories,
                                                 range(len(
                                                     table.columns[aggregationColumnIndex].valueCategories))):


            for cell, rowIndex in zip(table.columns[aggregationColumnIndex].cells[1:],
                                      range(1, len(table.columns[aggregationColumnIndex].cells))):
                if self.compareUtil(cell, categorizedValue):
                    targetAggRow = RowUtils.getRowFromTable(aggregatedBufferColumns, aggRowIndex + 1)

                    targetRow = RowUtils.getRowFromTable(table.columns, rowIndex)

                    bufferRow = RowUtils.addTwoCellsLists(targetAggRow, targetRow)

                    RowUtils.updateRowInTable(aggregatedBufferColumns, aggRowIndex + 1, bufferRow)

        table.aggregator.aggregatedTable = aggregatedBufferColumns
        return aggregatedBufferColumns

    @classmethod
    def __initAggregatedBufferColumns(cls, aggColumns: List[ColumnModel], aggColumnId: int, columns: List[ColumnModel]):
        # filling new aggregated columns with the aggregated column values.
        for column in columns:
            bufferNameCell = CellModel(column.name, enums.CellType.string.value)

            if column.id == aggColumnId:
                bufferColumn = ColumnModel([bufferNameCell], column.name, column.id, column.isDeleted)
                bufferColumn.columnType = deepcopy(column.columnType)
                bufferColumn.cells.extend(column.valueCategories)
                aggColumns.append(bufferColumn)
            else:
                bufferColumn = ColumnModel([bufferNameCell], column.name, column.id, column.isDeleted)
                bufferColumn.columnType = deepcopy(column.columnType)
                aggColumns.append(bufferColumn)

        # filling the reset of the columns with empty cells to be used when adding other rows to it.
        aggColumnIndex = DataController.getElementIndexById(aggColumns, aggColumnId)
        for i in range(1, len(aggColumns[aggColumnIndex].cells)):
            for column, j in zip(aggColumns, range(len(aggColumns))):
                if column.id != aggColumnId:
                    if columns[j].cells[i].type != enums.CellType.numeric.value:
                        column.cells.append(columns[j].cells[i])
                    else:
                        column.cells.append(CellModel(0, enums.CellType.numeric.value))


class DayBasedSumAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = filterAgent(data, 0, modelId)

        AggregationColumnUtils.updateDayBasedValueCats(filteredTable.columns[aggregationColumnIndex])

        aggregator = BasicSumAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameDay
        return aggregator.aggregateTable(filteredTable, aggregationBaseColumnId)


class MonthBasedSumAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = filterAgent(data, 0, modelId)

        AggregationColumnUtils.updateMonthBasedValueCats(filteredTable.columns[aggregationColumnIndex])

        aggregator = BasicSumAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameMonth
        return aggregator.aggregateTable(filteredTable, aggregationBaseColumnId)


class YearBasedSumAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:

        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = filterAgent(data, 0, modelId)

        AggregationColumnUtils.updateYearBasedValueCats(filteredTable.columns[aggregationColumnIndex])

        aggregator = BasicSumAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameYear
        return aggregator.aggregateTable(filteredTable, aggregationBaseColumnId)




class BasicAvgAggregation():
    def __init__(self):
        self.compareUtil = basicCompare

    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        filteredTable = filterAgent(data, 0, modelId)
        cols = cls.aggregateTable(filteredTable, aggregationBaseColumnId)
        return cols

    def aggregateTable(self, table: TableModel, aggregationBaseColumnId: int) -> List[ColumnModel]:
        aggregatedBufferColumns = list()

        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        table.columns[aggregationColumnIndex].valueCategories = \
            deepcopy(table.columns[aggregationColumnIndex].valueCategories)


        self.__initAggregatedBufferColumns(aggregatedBufferColumns, aggregationBaseColumnId,
                                           deepcopy(table.columns))

        for categorizedValue, aggRowIndex in zip(table.columns[aggregationColumnIndex].valueCategories,
                                                 range(len(
                                                     table.columns[aggregationColumnIndex].valueCategories))):
            counter = 0
            for cell, rowIndex in zip(table.columns[aggregationColumnIndex].cells[1:],
                                      range(1, len(table.columns[aggregationColumnIndex].cells))):
                if self.compareUtil(cell, categorizedValue):
                    targetAggRow = RowUtils.getRowFromTable(aggregatedBufferColumns, aggRowIndex + 1)

                    targetRow = RowUtils.getRowFromTable(table.columns, rowIndex)

                    bufferRow = RowUtils.addTwoCellsLists(targetAggRow, targetRow)
                    RowUtils.updateRowInTable(aggregatedBufferColumns, aggRowIndex + 1, bufferRow)
                    counter += 1

            RowUtils.updateRowInTable(aggregatedBufferColumns, aggRowIndex + 1,
                                      RowUtils.divideCellsListOnNum(
                                          RowUtils.getRowFromTable(aggregatedBufferColumns, aggRowIndex + 1), counter))

        table.aggregator.aggregatedTable = aggregatedBufferColumns
        return aggregatedBufferColumns


    @classmethod
    def __initAggregatedBufferColumns(cls, aggColumns: List[ColumnModel], aggColumnId: int, columns: List[ColumnModel]):
        # filling new aggregated columns with the aggregated column values.
        for column in columns:
            bufferNameCell = CellModel(column.name, enums.CellType.string.value)

            if column.id == aggColumnId:
                bufferColumn = ColumnModel([bufferNameCell], column.name, column.id, column.isDeleted)
                bufferColumn.columnType = deepcopy(column.columnType)
                bufferColumn.cells.extend(column.valueCategories)
                aggColumns.append(bufferColumn)
            else:
                bufferColumn = ColumnModel([bufferNameCell], column.name, column.id, column.isDeleted)
                bufferColumn.columnType = deepcopy(column.columnType)
                aggColumns.append(bufferColumn)

        # filling the reset of the columns with empty cells to be used when adding other rows to it.
        aggColumnIndex = DataController.getElementIndexById(aggColumns, aggColumnId)
        for i in range(1, len(aggColumns[aggColumnIndex].cells)):
            for column, j in zip(aggColumns, range(len(aggColumns))):
                if column.id != aggColumnId:
                    if columns[j].cells[i].type != enums.CellType.numeric.value:
                        column.cells.append(columns[j].cells[i])
                    else:
                        column.cells.append(CellModel(0, enums.CellType.numeric.value))


class DayBasedAvgAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = filterAgent(data, 0, modelId)

        AggregationColumnUtils.updateDayBasedValueCats(filteredTable.columns[aggregationColumnIndex])

        aggregator = BasicAvgAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameDay
        return aggregator.aggregateTable(filteredTable, aggregationBaseColumnId)


class MonthBasedAvgAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = filterAgent(data, 0, modelId)

        AggregationColumnUtils.updateMonthBasedValueCats(filteredTable.columns[aggregationColumnIndex])

        aggregator = BasicAvgAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameMonth
        return aggregator.aggregateTable(filteredTable, aggregationBaseColumnId)


class YearBasedAvgAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel,
                             aggregationBaseColumnId: int, filterAgent, modelId: int) -> List[ColumnModel]:
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = filterAgent(data, 0, modelId)

        AggregationColumnUtils.updateYearBasedValueCats(filteredTable.columns[aggregationColumnIndex])

        aggregator = BasicAvgAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameYear
        return aggregator.aggregateTable(filteredTable, aggregationBaseColumnId)


class AggregationColumnUtils():

    @classmethod
    def updateDayBasedValueCats(cls, column: ColumnModel):
        column.valueCategories.clear()
        for cell in column.cells[1:]:
            if not cls.__dayInList(cell, column.valueCategories):
                column.valueCategories.append(cell)

    @classmethod
    def updateMonthBasedValueCats(cls, column: ColumnModel):
        column.valueCategories.clear()
        for cell in column.cells[1:]:
            if not cls.__monthInList(cell, column.valueCategories):
                cellToAdd = CellModel(cell.value[:7], cell.type)
                column.valueCategories.append(cellToAdd)

    @classmethod
    def updateYearBasedValueCats(cls, column: ColumnModel):
        column.valueCategories.clear()
        for cell in column.cells[1:]:
            if not cls.__yearInList(cell, column.valueCategories):
                cellToAdd = CellModel(cell.value[:4], cell.type)
                column.valueCategories.append(cellToAdd)

    @classmethod
    def sameDay(cls, cell1: CellModel, cell2: CellModel) -> bool:
        buffer1 = parse(cell1.value)
        buffer2 = parse(cell2.value)
        if (buffer1.day == buffer2.day) and (buffer1.month == buffer2.month) and (buffer1.year == buffer2.year):
            return True
        return False

    @classmethod
    def sameMonth(cls, cell1: CellModel, cell2: CellModel) -> bool:
        buffer1 = parse(cell1.value)
        buffer2 = parse(cell2.value)
        if (buffer1.month == buffer2.month) and (buffer1.year == buffer2.year):
            return True
        return False

    @classmethod
    def sameYear(cls, cell1: CellModel, cell2: CellModel) -> bool:
        buffer1 = parse(cell1.value)
        buffer2 = parse(cell2.value)
        if (buffer1.year == buffer2.year):
            return True
        return False

    @classmethod
    def __dayInList(cls, cell: CellModel, column: List[CellModel]):
        for c in column:
            if cls.sameDay(c, cell):
                return True
        return False

    @classmethod
    def __monthInList(cls, cell: CellModel, column: List[CellModel]):
        for c in column:
            if cls.sameMonth(c, cell):
                return True
        return False

    @classmethod
    def __yearInList(cls, cell: CellModel, column: List[CellModel]):
        for c in column:
            if cls.sameYear(c, cell):
                return True
        return False


class AggregationFactory():
    @classmethod
    def getAggregator(cls, type: str):
        if type == enums.AggregationType.BasicSum.value:
            aggregator = BasicSumAggregation()
            aggregator.compareUtil = basicCompare
            return aggregator

        if type == enums.AggregationType.DayBasedSum.value:
            return DayBasedSumAggregation()

        if type == enums.AggregationType.MonthBasedSum.value:
            return MonthBasedSumAggregation()

        if type == enums.AggregationType.YearBasedSum.value:
            return YearBasedSumAggregation()

        if type == enums.AggregationType.BasicAvg.value:
            aggregator = BasicAvgAggregation()
            aggregator.compareUtil = basicCompare
            return aggregator

        if type == enums.AggregationType.DayBasedAvg.value:
            return DayBasedAvgAggregation()

        if type == enums.AggregationType.MonthBasedAvg.value:
            return MonthBasedAvgAggregation()

        if type == enums.AggregationType.YearBasedAvg.value:
            return YearBasedAvgAggregation()


def getAggregator(type: str):
    return AggregationFactory.getAggregator(type)


def clearAggregationTable(table: TableModel):
    table.aggregator.aggregatedTable.clear()


def setAggregationOn(table: TableModel):
    table.aggregator.isActive = True


def setAggregationOff(table: TableModel):
    table.aggregator.isActive = False


def basicCompare(cell: CellModel, valueCat: CellModel) -> bool:
    if cell.value == valueCat.value:
        return True
    return False
