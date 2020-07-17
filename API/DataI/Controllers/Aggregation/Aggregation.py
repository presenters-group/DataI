from typing import List

from DataI import enums
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DataControllers.DataSourcesController import DataSourcesController
from DataI.Models.ColumnModel import CellModel, ColumnModel
from DataI.Models.TableModel import TableModel


class BasicAggregationController():

    @classmethod
    def implementAggregation(cls, table: TableModel, aggregationBaseColumnId: int):
        aggregatedBufferColumns = list()

        cls.__initAggregatedBufferColumns(aggregatedBufferColumns, aggregationBaseColumnId, table.columns)

        for column in aggregatedBufferColumns:
            print('column name:', column.name)
            for cell in column.cells:
                print(cell)
            print('____________________________')


        aggregationColumnIndex = DataController.getElementIndexById(table.columns, aggregationBaseColumnId)

        for categorizedValue in table.columns[aggregationColumnIndex].valueCategories:
            bufferRow = list()
            for cell, rowIndex in zip(table.columns[aggregationColumnIndex].cells,
                               range(len(table.columns[aggregationColumnIndex].cells))):
                if cell.value == categorizedValue.value:
                    pass


    @classmethod
    def __initAggregatedBufferColumns(cls, aggColumns: List[CellModel], aggColumnId: int, columns: List[ColumnModel]):

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









