import json
import os
import re

from numpy import double

from DataI import enums
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DataControllers.DataSourcesController import DataSourcesController
from DataI.Controllers.DrawControllers.DrawController import DrawController
from DataI.Controllers.Filters.FilterController import NumericFilter, MultipleEqualityFilter, FiltersController
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.ColumnModel import CellModel
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.FilterModel import FilterModel
import os

from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.DrawController import DrawController
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.VisualizationModel import VisualizationModel


dataController = DataController()
dirName = os.path.dirname(__file__)
filename = os.path.join(dirName, '../Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

jsonFilters = '''
[
        {
            "name": "filter1",
            "id": 0,
            "dataSource": 0,
            "filteredColumn": 0,
            "initValue": "A",
            "type": "MultipleEquality",
            "isDeleted": false
        },
        {
            "name": "filter2",
            "id": 1,
            "dataSource": 0,
            "filteredColumn": 2,
            "initValue": 100,
            "type": ">",
            "isDeleted": false
        },
        {
            "name": "filter3",
            "id": 2,
            "dataSource": 0,
            "filteredColumn": 0,
            "initValue": 11,
            "type": "<",
            "isDeleted": false
        }
    ]
'''
jsonVisio = '''
{
            "name": "visualization1",
            "id": 0,
            "data": 0,
            "usedColumns": [
                0,
                1,
                2
            ],
            "xColumn": 0,
            "chart": "VerticalBarChart",
            "filters": [
                {
                    "id": 1,
                    "value": 5,
                    "isActive": true
                },
                {
                    "id": 0,
                    "value": "testerValue",
                    "isActive": true
                },
                {
                    "id": 2,
                    "value": 2142,
                    "isActive": false
                }
            ],
            "isDeleted": false
        }
'''

loadedJsonFilters = json.loads(jsonFilters)
for filter in loadedJsonFilters:
    dataController.data.filters.append(FilterModel.from_json(filter))

filter1 = {
    "id": 1,
    "value": 50,
    "isActive": True
}
filter2 = {
    "id": 1,
    "value": 60,
    "isActive": False
}
filter3 = {
    "id": 0,
    "value": ['log', '44', '15'],
    "isActive": True
}

dataController.data.visualizations.append(VisualizationModel.from_json(json.loads(jsonVisio)))
dataController.data.dataSources[0].filters = [filter1, filter2, filter3]
dataController.data.dataSources[1].filters = [filter3]
dataController.data.visualizations[0].filters = [filter1]

index = DataController.getElementIndexFromDictById(dataController.data.dataSources[0].filters, 0)

print(dataController.data.dataSources[0].filters[index])

# for color in dataController.data.dataSources[0].rowsColors:

#filteredTable = FiltersController.getFilteredTable(dataController.data, 0)

# print(len(filteredTable.rowsColors))
# print(len(filteredTable.columns[0].cells))
# filteredTables = DataSourcesController.getFinalTables(dataController.data)
#
# for table in filteredTables:
#     for column in table.columns:
#         for cell in column.cells:
#             print(cell)
#         print('_________________')
#     print('==================================')
#     print('__________________________________')
#     print('==================================')


# for column in dataController.data.dataSources[0].columns:
#     for cell in column.cells:
#         print(cell)
#     print('____________________________')

# filter = MultipleEqualityFilter()
# filter = NumericFilter('>')

# filteredTable= filter.implementFilter(dataController.data.dataSources[0], 2, [51, 15, 44])

# for column in filteredTable.columns:
#     for cell in column.cells:
#         print(cell)
#     print('__________________________')






#
# # load static data:
# jsonVisio = '''
# {
#             "name": "visualization1",
#             "id": 0,
#             "data": 0,
#             "usedColumns": [
#                 0,
#                 1,
#                 2
#             ],
#             "xColumn": 0,
#             "chart": "MultiplePieChart",
#             "filters": [
#                 {
#                     "id": 1,
#                     "value": 5
#                 },
#                 {
#                     "id": 0,
#                     "value": "testerValue"
#                 },
#                 {
#                     "id": 2,
#                     "value": 2142
#                 }
#             ],
#             "isDeleted": false
#         }
# '''
# jsonDashboard = '''
# {
#             "name": "dashboard1",
#             "id": 0,
#             "visualizers": [
#                 {
#                     "visualizationIndex": 0,
#                     "measurements": {
#                         "width": 1.0,
#                         "height": 1.0,
#                         "x": 1.0,
#                         "y": 1.0
#                     },
#                     "displayedFilters": [
#                         {
#                             "filterIndex": 0,
#                             "measurements": {
#                                 "width": 0.0,
#                                 "height": 0.0,
#                                 "x": 0.0,
#                                 "y": 0.0
#                             }
#                         },
#                         {
#                             "filterIndex": 1,
#                             "measurements": {
#                                 "width": 1.0,
#                                 "height": 1.0,
#                                 "x": 1.0,
#                                 "y": 1.0
#                             }
#                         }
#                     ]
#                 }
#             ],
#             "isDeleted": false
#         }
# '''
# jsonFilters = '''
# [
#         {
#             "name": "filter1",
#             "id": 0,
#             "dataSource": 0,
#             "filteredColumn": 1,
#             "initValue": "A",
#             "type": "Equality",
#             "isDeleted": false
#         },
#         {
#             "name": "filter2",
#             "id": 1,
#             "dataSource": 0,
#             "filteredColumn": 2,
#             "initValue": 100,
#             "type": "LessThan",
#             "isDeleted": false
#         },
#         {
#             "name": "filter3",
#             "id": 2,
#             "dataSource": 0,
#             "filteredColumn": 0,
#             "initValue": 11,
#             "type": "MoreThan",
#             "isDeleted": false
#         }
#     ]
# '''
#
# dataController.data.visualizations.append(VisualizationModel.from_json(json.loads(jsonVisio)))
# dataController.data.dashboards.append(DashboardModel.from_json(json.loads(jsonDashboard)))
# loadedJsonFilters = json.loads(jsonFilters)
# for filter in loadedJsonFilters:
#   dataController.data.filters.append(FilterModel.from_json(filter))
#
# drawTable = DrawController.generateVisualizerTable(dataController.data, 0)
#
# # for column in drawTable.columns:
# #   for cell in column.cells:
# #     print(cell.value)
# #     print(cell.type)
# #     print(type(cell.value))
#
#
# print('________')
# print('________')
# print('________')
#
#
# for col in dataController.data.dataSources[0].columns:
#   print(col.columnType)
#   print(col.cells[2])
#
#
# string = '100.k0'
# isDigit = string.replace('.', '').isdigit()
# print(isDigit)
# svgString = DrawController.getSVGString(dataController.data, 0, double(10), double(1000))
#

# print(svgString)



# from DataI import enums
# from DataI.Models.ColumnModel import CellModel, ColumnModel
#
# cell1 = CellModel(10, enums.CellType.numeric.value)
# cell2 = CellModel(20, enums.CellType.numeric.value)
#
# cells = [cell1, cell2, cell2, cell2, cell2, cell2]
#
# column1 = ColumnModel(cells, 'name', 10, None, False)
# column2 = ColumnModel(cells, 'name', 10, None, False)
#
# column = column1 + column2
#
# for cell in column.cells:
#   print(cell)


# data = -1
# isDigit = str(data).replace('.', '').isdigit() or str(data).replace('-', '').isdigit()
# print(isDigit)
# print(str(data).replace('-', ''))
# print(data)
# print(type(data))














