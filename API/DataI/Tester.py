import json
import os
import re

from numpy import double

from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.DrawController import DrawController
from DataI.Controllers.Filters.FilterController import NumericFilterController
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

filter = NumericFilterController()

filteredColumn = filter.implementFilter(dataController.data.dataSources[0].columns[0], '<', 10)

for cell in filteredColumn.cells:
    print(cell)



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














