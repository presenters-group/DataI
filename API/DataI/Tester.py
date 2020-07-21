import json
import os

from DataI import enums
from DataI.Controllers.Aggregation.Aggregation import BasicAggregation, AggregationColumnUtils, DayBasedAggregation, \
    MonthBasedAggregation, YearBasedAggregation
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.DrawController import DrawController
from DataI.Controllers.Equation.Equation import Equation
from DataI.Controllers.FileSaver.DataIFileSaver import DataIFileSaver
from DataI.Controllers.Filters.FiltersController import FiltersController
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.ColumnModel import ColumnModel, CellModel
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel
dataController = DataController()
# dirName = os.path.dirname(__file__)
# filename = os.path.join(dirName, 'binary-test-file.datai')
# dataController.loadDataIFile(filename)




dirName = os.path.dirname(__file__)
filename = os.path.join(dirName, '../Aggregation-Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

# ================================ load static data ================================:


jsonVisio1 = '''
{
            "name": "visualization1",
            "id": 0,
            "data": 0,
            "usedColumns": [
                0,
                2,
                3
            ],
            "xColumn": 0,
            "chart": "BoundaryLineChart",
            "filters": [
            ],
            "isDeleted": false,
            "animation": false
}
'''
jsonVisio2 = '''
{
            "name": "visualization2",
            "id": 1,
            "data": 0,
            "usedColumns": [
                0,
                2,
                3
            ],
            "xColumn": 0,
            "chart": "VerticalBarChart",
            "filters": [
            ],
            "isDeleted": false,
            "animation": true
}
'''

jsonDashboard = '''
{
	"name": "dashboard1",
	"id": 0,
	"isDeleted": false,
	"visualizers": [{
			"visualizationId": 0,
			"measurements": {
				"width": 100.0,
				"height": 100.0,
				"x": 50.0,
				"y": 60.0
			}
		},
		{
			"visualizationId": 1,
			"measurements": {
				"width": 100.0,
				"height": 100.0,
				"x": 50.0,
				"y": 60.0
			}
		}
	],
	"filters": [{
		"id": 1,
		"visioId": 0,
		"value": 50,
		"isActive": true,
		"measurements": {
			"width": 20.0,
			"height": 60.0,
			"x": 10.0,
			"y": 20.0
		}
	}]
}
'''

jsonFilters = '''
[
        {
            "name": "filter1",
            "id": 0,
            "dataSource": 1,
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
            "filteredColumn": 3,
            "initValue": 11,
            "type": "<",
            "isDeleted": false
        },
        {
            "name": "dateTimeFilter",
            "id": 3,
            "dataSource": 0,
            "filteredColumn": 1,
            "initValue": "11/10/2000",
            "type": ">",
            "isDeleted": false
        }
]
'''

filter1 = {
    "id": 1,
    "value": 50,
    "isActive": True
}
filter2 = {
    "id": 2,
    "value": 60,
    "isActive": False
}
filter3 = {
    "id": 0,
    "value": ['log', '44', '15'],
    "isActive": True
}


dataController.data.visualizations.append(VisualizationModel.from_json(json.loads(jsonVisio1)))
dataController.data.visualizations.append(VisualizationModel.from_json(json.loads(jsonVisio2)))
dataController.data.dashboards.append(DashboardModel.from_json(json.loads(jsonDashboard)))
loadedJsonFilters = json.loads(jsonFilters)
for filter in loadedJsonFilters:
    dataController.data.filters.append(FilterModel.from_json(filter))


dateTimeFilter = {
    "id": 3,
    "value": '7/23/2020',
    "isActive": True
}

dataController.data.dataSources[0].printTable()

print('=========================================================================================================')
print('=========================================================================================================')


equation = '( السعر + الحجم ) * ( السعر - الكمية )'

Equation.implementEquation(dataController.data.dataSources[0], equation, 'EquationResult')

dataController.data.dataSources[0].printTable()

# dataController.data.dataSources[0].filters.append(dateTimeFilter)

# table = FiltersController.getFilteredTable(dataController.data, 0)
#
# table.printTable()
#
# print('=========================================================================================================')
# print('=========================================================================================================')
#
# # DayBasedAggregation.implementAggregation(dataController.data, table, 1)
# # MonthBasedAggregation.implementAggregation(dataController.data, table, 1)
# # YearBasedAggregation.implementAggregation(dataController.data, table, 1)
# # aggregator = BasicAggregation()
# # aggregator.implementAggregation(dataController.data, table, 0)
#
# print('=========================================================================================================')
# print('=========================================================================================================')
#
# TableModel.printColumns(table.aggregator.aggregatedTable)


# print(dataController.data.dataSources[0].columns[0].name + ':', dataController.data.dataSources[0].columns[0].columnType)
# print(dataController.data.dataSources[0].columns[1].name + ':', dataController.data.dataSources[0].columns[1].columnType)
# print(dataController.data.dataSources[0].columns[2].name + ':', dataController.data.dataSources[0].columns[2].columnType)
# print(dataController.data.dataSources[0].columns[3].name + ':', dataController.data.dataSources[0].columns[3].columnType)
# print(dataController.data.dataSources[0].columns[4].name + ':', dataController.data.dataSources[0].columns[4].columnType)


# for c in dataController.data.dataSources[0].columns[1].cells:
#     print(c.value, c.type, type(c.value))

# dateColumn = ColumnModel(
#     [
#         CellModel('Date', enums.CellType.string.value),
#         CellModel('22/1/2000', enums.CellType.string.value),
#         CellModel('10/2/2000', enums.CellType.string.value),
#         CellModel('15/10/2001', enums.CellType.string.value),
#         CellModel('17/10/2001', enums.CellType.string.value),
#         CellModel('2/7/2002', enums.CellType.string.value),
#         CellModel('4/8/2002', enums.CellType.string.value)
#     ], 'Date', 0, False
# )


# dateColumn = dataController.data.dataSources[0].columns[1]
# AggregationColumnUtils.updateDayBasedValueCats(dateColumn)
# for ce in dateColumn.valueCategories:
#     print(ce)
# print('__________________________________________________________________')
# AggregationColumnUtils.updateMonthBasedValueCats(dateColumn)
# for ce in dateColumn.valueCategories:
#     print(ce)
# print('__________________________________________________________________')
# AggregationColumnUtils.updateYearBasedValueCats(dateColumn)
# for ce in dateColumn.valueCategories:
#     print(ce)
# print('__________________________________________________________________')
#




# BasicAggregationController.implementAggregation(dataController.data.dataSources[0], 0)
#
#
# for col in dataController.data.dataSources[0].aggregator.aggregatedTable:
#     for c in col.cells:
#         print(c)
#     print('_________________________')


# for column in dataController.data.dataSources[0].columns:
#     print('column type: ', column.columnType)
#     for c in column.cells:
#         print(c)
#     print('_____________________________')
#
# print('===================================')
#
# for column in dataController.data.dataSources[0].columns:
#     for c in column.valueCategories:
#         print(c)
#     print('_____________________________')






# for column in filteredTable.columns:
#     for cell in column.cells:
#         print(cell)
#     print('__________________________')


# for color in dataController.data.dataSources[0].rowsColors:

#filteredTable = FiltersController.getFilteredTable(dataController.data, 0)

# print(len(filteredTable.rowsColors))
# print(len(filteredTable.columns[0].cells))
# filteredTables = DataSourcesController.getFinalTables(dataController.data)

# for table in dataController.data.dataSources:
#     for column in table.columns:
#         print('Column Type: {}'.format(column.columnType))
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



























# measure = Measurements(20.0, 60.0, 10.0, 20.0)
# inDashFilter1 = InDashboardFilterModel(0, 0, 50, True, measure)
# inDashFilter2 = InDashboardFilterModel(1, 0, 50, True, measure)
# measure = Measurements(100.0, 100.0, 50.0, 60.0)
# inVisio = InDashboardVisioModel(0, measure)
#
# dashboard = DashboardModel([inVisio], 'dashboard1', 0, [inDashFilter1, inDashFilter2], False)
#
# jsonDash = json.dumps(dashboard, indent=4, cls=ObjectEncoder, ensure_ascii=False)
#
# print(jsonDash)





