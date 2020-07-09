import operator
from copy import deepcopy
from typing import List

from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.DataControllers import DataSourcesController
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel


class NumericFilter():
    def __init__(self, operator: str):
        self.operator = operator

    def implementFilter(self, table: TableModel, columnId: int, value) -> TableModel:
        operators = {
            '=': operator.eq,
            'is': operator.eq,
            '!=': operator.is_not,
            'is not': operator.is_not,
            '<=': operator.le,
            '<': operator.lt,
            '>=': operator.ge,
            '>': operator.gt,
        }

        filteredTable = deepcopy(table)
        columnIndex = DataController.getElementIndexById(table.columns,columnId)
        column = filteredTable.columns[columnIndex]

        rowCounter = 1
        for cell in column.cells[1:]:
            if not operators[self.operator](cell.value, value):
                DataSourcesController.removeRowFromTable(filteredTable, rowCounter)
                # refresh row counter after deleting
                rowCounter -= 1
            rowCounter += 1


        return filteredTable


class MultipleEqualityFilter():
    def implementFilter(self, table: TableModel, columnId: int, values: List) -> TableModel:

        filteredTable = deepcopy(table)
        columnIndex = DataController.getElementIndexById(table.columns, columnId)
        column = filteredTable.columns[columnIndex]

        rowCounter = 1
        for cell in column.cells[1:]:
            if cell.value not in values:
                DataSourcesController.removeRowFromTable(filteredTable, rowCounter)
                # refresh row counter after deleting
                rowCounter -= 1
            rowCounter += 1


        return filteredTable


class FiltersController():
    @classmethod
    def getFilteredTable(cls, data: DataModel, tableId: int) -> TableModel:
        tableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        table = data.dataSources[tableIndex]
        filteredTable = deepcopy(table)

        for tableFilter in table.filters:
            filterModelIndex = DataController.getElementIndexById(data.filters, tableFilter['id'])
            filterModel = data.filters[filterModelIndex]

            if tableFilter['isActive']:
                filterObj = FiltersFactory.getFilter(filterModel.type)
                filteredTable = filterObj.implementFilter(filteredTable, filterModel.filteredColumn, tableFilter['value'])

        return filteredTable

    @classmethod
    def __appendNonFilteredColumns(cls, columnsList: List[ColumnModel], table: TableModel):
        # getting filtered columns IDs in a list for comparison.
        filteredColumnsIDs = list()
        for column in columnsList:
            filteredColumnsIDs.append(column.id)

        tableColumnsIDs = list()
        for column in table.columns:
            tableColumnsIDs.append(column.id)

        for id in tableColumnsIDs:
            if id not in filteredColumnsIDs:
                columnIndex = DataController.getElementIndexById(table.columns, id)
                column = table.columns[columnIndex]
                columnsList.append(column)







class FiltersFactory():
    @classmethod
    def getFilter(cls, filterType: str):
        if filterType == 'MultipleEquality':
            return MultipleEqualityFilter()
        else:
            return NumericFilter(filterType)