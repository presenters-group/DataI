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


class BasicAggregation():

    def __init__(self):
        self.compareUtil = basicCompare

    def implementAggregation(self, data: DataModel, table: TableModel, aggregationBaseColumnId: int):
        aggregatedBufferColumns = list()

        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        filteredTable = FiltersController.getFilteredTable(data, table.id)

        filteredTable.columns[aggregationColumnIndex].valueCategories = \
            deepcopy(table.columns[aggregationColumnIndex].valueCategories)

        self.__initAggregatedBufferColumns(aggregatedBufferColumns, aggregationBaseColumnId,
                                          deepcopy(table.columns))

        for categorizedValue, aggRowIndex in zip(filteredTable.columns[aggregationColumnIndex].valueCategories,
                                                 range(len(
                                                     filteredTable.columns[aggregationColumnIndex].valueCategories))):

            for cell, rowIndex in zip(filteredTable.columns[aggregationColumnIndex].cells[1:],
                                      range(1, len(filteredTable.columns[aggregationColumnIndex].cells))):
                if self.compareUtil(cell, categorizedValue):
                    targetAggRow = RowUtils.getRowFromTable(aggregatedBufferColumns, aggRowIndex + 1)

                    targetRow = RowUtils.getRowFromTable(filteredTable.columns, rowIndex)

                    bufferRow = RowUtils.addTwoCellsLists(targetAggRow, targetRow)
                    RowUtils.updateRowInTable(aggregatedBufferColumns, aggRowIndex + 1, bufferRow)

        table.aggregator.aggregatedTable = aggregatedBufferColumns


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


class DayBasedAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel, aggregationBaseColumnId: int):
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)
        AggregationColumnUtils.updateDayBasedValueCats(table.columns[aggregationColumnIndex])

        aggregator = BasicAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameDay
        aggregator.implementAggregation(data, table, aggregationBaseColumnId)


class MonthBasedAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel, aggregationBaseColumnId: int):
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)
        AggregationColumnUtils.updateMonthBasedValueCats(table.columns[aggregationColumnIndex])

        aggregator = BasicAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameMonth
        aggregator.implementAggregation(data, table, aggregationBaseColumnId)


class YearBasedAggregation():
    @classmethod
    def implementAggregation(cls, data: DataModel, table: TableModel, aggregationBaseColumnId: int):
        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)
        AggregationColumnUtils.updateYearBasedValueCats(table.columns[aggregationColumnIndex])

        aggregator = BasicAggregation()
        aggregator.compareUtil = AggregationColumnUtils.sameYear
        aggregator.implementAggregation(data, table, aggregationBaseColumnId)


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
        if type == enums.AggregationType.Basic.value:
            aggregator = BasicAggregation()
            aggregator.compareUtil = basicCompare
            return aggregator

        if type == enums.AggregationType.DayBased.value:
            return DayBasedAggregation()

        if type == enums.AggregationType.MonthBased.value:
            return MonthBasedAggregation()

        if type == enums.AggregationType.YearBased.value:
            return YearBasedAggregation()


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




