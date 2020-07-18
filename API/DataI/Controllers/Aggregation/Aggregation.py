from typing import List

from DataI import enums
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DataControllers import DataSourcesController
from DataI.Models.ColumnModel import CellModel, ColumnModel
from DataI.Models.TableModel import TableModel


class AggregationController():
    @classmethod
    def clearAggregationTable(cls, table: TableModel):
        table.aggregator.aggregatedTable.clear()

    @classmethod
    def setAggregationOn(cls, table: TableModel):
        table.aggregator.isActive = True

    @classmethod
    def setAggregationOff(cls, table: TableModel):
        table.aggregator.isActive = False



class BasicAggregationController():

    @classmethod
    def implementAggregation(cls, table: TableModel, aggregationBaseColumnId: int):
        aggregatedBufferColumns = list()

        cls.__initAggregatedBufferColumns(aggregatedBufferColumns, aggregationBaseColumnId, table.columns)

        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)


        # for column in aggregatedBufferColumns:
        #     #print('column name:', column.name)
        #     for cell in column.cells:
        #         print(cell)
        #     print('____________________________')


        for categorizedValue, aggRowIndex in zip(table.columns[aggregationColumnIndex].valueCategories,
                                              range(len(table.columns[aggregationColumnIndex].valueCategories))):

            for cell, rowIndex in zip(table.columns[aggregationColumnIndex].cells[1:],
                                      range(1, len(table.columns[aggregationColumnIndex].cells))):
                if cell.value == categorizedValue.value:
                    targetAggRow = DataSourcesController.getRowFromTable(aggregatedBufferColumns, aggRowIndex + 1)
                    targetRow = DataSourcesController.getRowFromTable(table.columns, rowIndex)
                    bufferRow = DataSourcesController.addTwoCellsLists(targetAggRow, targetRow)
                    DataSourcesController.updateRowInTable(aggregatedBufferColumns, aggRowIndex + 1, bufferRow)


        table.aggregator.aggregatedTable = aggregatedBufferColumns




    @classmethod
    def __initAggregatedBufferColumns(cls, aggColumns: List[ColumnModel], aggColumnId: int, columns: List[ColumnModel]):

        # filling new aggregated columns with the aggregated column values.
        for column in columns:
            bufferNameCell = CellModel(column.name, enums.CellType.string.value)

            if column.id == aggColumnId:
                bufferColumn = ColumnModel([bufferNameCell], column.name, column.id, column.isDeleted)
                bufferColumn.cells.extend(column.valueCategories)
                aggColumns.append(bufferColumn)
            else:
                aggColumns.append(ColumnModel([bufferNameCell], column.name, column.id, column.isDeleted))

        # filling the reset of the columns with empty cells to be used when adding other rows to it.
        aggColumnIndex = DataController.getElementIndexById(aggColumns, aggColumnId)
        for i in range(1, len(aggColumns[aggColumnIndex].cells)):
            for column in aggColumns:
                if column.id != aggColumnId:
                    column.cells.append(CellModel(0, enums.CellType.numeric.value))









