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
                filteredTable.rowsColors.pop(rowCounter - 1)
                # refresh row counter after deleting
                rowCounter -= 1
            rowCounter += 1

        for column in filteredTable.columns:
            DataSourcesController.updateCategorizedValues(column)

        return filteredTable


class MultipleEqualityFilter():
    def implementFilter(self, table: TableModel, columnId: int, values: List) -> TableModel:

        filteredTable = deepcopy(table)
        columnIndex = DataController.getElementIndexById(table.columns, columnId)
        column = filteredTable.columns[columnIndex]

        values = self.__castNumericListElementsToFloats(values)

        rowCounter = 1
        for cell in column.cells[1:]:
            if cell.value not in values:
                print('rows: ' + str(len(filteredTable.columns[0].cells)))
                print('rows colors: ' + str(len(filteredTable.rowsColors)))
                print('row counter: ' + str(rowCounter))
                DataSourcesController.removeRowFromTable(filteredTable, rowCounter)
                filteredTable.rowsColors.pop(rowCounter - 1)
                # refresh row counter after deleting
                rowCounter -= 1
            rowCounter += 1

        for column in filteredTable.columns:
            DataSourcesController.updateCategorizedValues(column)

        return filteredTable

    def __castNumericListElementsToFloats(self, values: List) -> List:
        newList = list()
        for element in values:
            isDigit = str(element).replace('.', '').isdigit() or str(element).replace('-', '').isdigit()
            if isDigit:
                newList.append(float(element))
            else:
                newList.append(element)
        return newList


class FiltersController():
    @classmethod
    def getFilteredTable(cls, data: DataModel, tableId: int) -> TableModel:
        tableIndex = DataController.getElementIndexById(data.dataSources, tableId)
        table = data.dataSources[tableIndex]
        filteredTable = deepcopy(table)

        for tableFilter in table.filters:
            filterModelIndex = DataController.getElementIndexById(data.filters, tableFilter['id'])
            filterModel = data.filters[filterModelIndex]

            if tableFilter['isActive'] and not filterModel.isDeleted:
                filterObj = FiltersFactory.getFilter(filterModel.type)
                filteredTable = filterObj.implementFilter(filteredTable, filterModel.filteredColumn, tableFilter['value'])

        return filteredTable

    @classmethod
    def getFilteredVisioTable(cls, data: DataModel, visioId: int) -> TableModel:
        visioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        visio = data.visualizations[visioIndex]
        tableIndex = DataController.getElementIndexById(data.dataSources, visio.data)
        table = data.dataSources[tableIndex]
        filteredTable = deepcopy(table)

        for visioFilter in visio.filters:
            filterModelIndex = DataController.getElementIndexById(data.filters, visioFilter['id'])
            filterModel = data.filters[filterModelIndex]

            if visioFilter['isActive'] and not filterModel.isDeleted:
                filterObj = FiltersFactory.getFilter(filterModel.type)
                filteredTable = filterObj.implementFilter(filteredTable, filterModel.filteredColumn, visioFilter['value'])

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