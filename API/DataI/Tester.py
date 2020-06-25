# import json
# import os
#
# from numpy import double
#
# from DataI.Controllers.DataControllers.DataController import DataController
# from DataI.Controllers.DrawControllers.DrawController import DrawController
# from DataI.Models.DashboardModel import DashboardModel
# from DataI.Models.FilterModel import FilterModel
# import os
#
# from DataI.Controllers.DataControllers.DataController import DataController
# from DataI.Controllers.DrawControllers.DrawController import DrawController
# from DataI.Models.DashboardModel import DashboardModel
# from DataI.Models.FilterModel import FilterModel
# from DataI.Models.VisualizationModel import VisualizationModel
#
# dataController = DataController()
# dirName = os.path.dirname(__file__)
# filename = os.path.join(dirName, '../Test.xlsx')
#
# dataController.loadTablesFromExcelFile(filename, 0)
#
# # load static data:
# jsonVisio = '''
# {
#             "name": "visualization1",
#             "id": 0,
#             "data": 0,
#             "usedColumns": [
#                 0,
#                 2
#             ],
#             "xColumn": 0,
#             "chart": "verticalBarChart",
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
#
# drawTable = DrawController.generateVisualizerTable(dataController.data, 0)
#
#
# print(drawTable)
# print(drawTable.columns[0].name)
# print(drawTable.columns[1].name)
#
# svgString = DrawController.getSVGString(dataController.data, 0, double(10), double(1000))
#
# print(svgString)
#


string = '''
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<svg xmlns=\"http://www.w3.org/2000/svg\"
	xmlns:xlink=\"http://www.w3.org/1999/xlink\"\n width=\"1400\" height=\"1000\" viewBox=\"0 -1000 1400 1000\">\n<defs>
		\n</defs>\n
	<rect x=\"0\" y=\"-1000\" width=\"1400\" height=\"1000\" fill=\"#ffffff\" />\n
	<rect x=\"0\" y=\"-1000\" width=\"1400\" height=\"1000\" fill=\"#ffffff\" />\n
	<path d=\"M200,-200.0 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-314.63521188291827 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />
	\n
	<path d=\"M200,-429.27042376583654 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />
	\n
	<path d=\"M200,-543.9056356487549 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-658.5408475316731 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-773.1760594145916 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-887.8112712975098 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-1002.4464831804282 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />
	\n
	<circle cx=\"350\" cy=\"-507.55788553953687\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\"
		id=\"0\" />\n
	<circle cx=\"500\" cy=\"-556.4875491480996\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\"
		id=\"1\" />\n
	<circle cx=\"650\" cy=\"-577.4574049803407\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\"
		id=\"2\" />\n
	<circle cx=\"800\" cy=\"-423.6784622105723\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\"
		id=\"3\" />\n
	<circle cx=\"950\" cy=\"-885.0152905198776\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\"
		id=\"4\" />\n
	<circle cx=\"1100\" cy=\"-654.346876365225\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\"
		id=\"5\" />\n
	<circle cx=\"1250\" cy=\"-200.0\" r=\"5\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\" id=\"6\" />\n
	<circle cx=\"350\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"344.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"7\">0</text>\n
	<circle cx=\"500\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"488.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"8\">15</text>\n
	<circle cx=\"650\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"644.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"9\">0</text>\n
	<circle cx=\"800\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"788.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"10\">33</text>\n
	<circle cx=\"950\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"944.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"11\">2</text>\n
	<circle cx=\"1100\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"1082.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"12\">111</text>\n
	<circle cx=\"1250\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"1238.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"13\">22</text>\n
	<circle cx=\"30\" cy=\"-58.0\" r=\"12\" fill=\"gray\" stroke-width=\"5\" stroke=\"black\" />\n<text x=\"55\"
		y=\"-50.0\" font-size=\"20.0\" id=\"14\">السعر</text>\n
	<circle cx=\"180\" cy=\"-58.0\" r=\"15\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"205\"
		y=\"-50.0\" font-size=\"20.0\" id=\"14\">الكمية</text>\n
	<circle cx=\"200\" cy=\"-200.0\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />\n<text
		x=\"57.142857142857146\" y=\"-200.0\" font-size=\"20\" id=\"14\">0.0</text>\n
	<circle cx=\"200\" cy=\"-314.63521188291827\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-314.63521188291827\" font-size=\"20\" id=\"15\">16.4</text>\n
	<circle cx=\"200\" cy=\"-429.27042376583654\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-429.27042376583654\" font-size=\"20\" id=\"16\">32.8</text>\n
	<circle cx=\"200\" cy=\"-543.9056356487549\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-543.9056356487549\" font-size=\"20\" id=\"17\">49.19999...</text>\n
	<circle cx=\"200\" cy=\"-658.5408475316731\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-658.5408475316731\" font-size=\"20\" id=\"18\">65.6</text>\n
	<circle cx=\"200\" cy=\"-773.1760594145916\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-773.1760594145916\" font-size=\"20\" id=\"19\">82.0</text>\n
	<circle cx=\"200\" cy=\"-887.8112712975098\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-887.8112712975098\" font-size=\"20\" id=\"20\">98.4</text>\n
	<rect x=\"0\" y=\"-1000\" width=\"1400\" height=\"1000\" fill=\"#ffffff\" />\n
	<path d=\"M425.0,-200.0 L425.0,-507.55788553953687 H450.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\"
		fill=\"#b3d168\" fill-opacity=\"0.5\" id=\"21\" />\n
	<path d=\"M575.0,-200.0 L575.0,-556.4875491480996 H600.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\"
		fill=\"#b3d168\" fill-opacity=\"0.5\" id=\"22\" />\n
	<path d=\"M725.0,-200.0 L725.0,-577.4574049803407 H750.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\"
		fill=\"#b3d168\" fill-opacity=\"0.5\" id=\"23\" />\n
	<path d=\"M875.0,-200.0 L875.0,-423.6784622105723 H900.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\"
		fill=\"#b3d168\" fill-opacity=\"0.5\" id=\"24\" />\n
	<path d=\"M1025.0,-200.0 L1025.0,-885.0152905198776 H1050.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\"
		fill=\"#b3d168\" fill-opacity=\"0.5\" id=\"25\" />\n
	<path d=\"M1175.0,-200.0 L1175.0,-654.346876365225 H1200.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\"
		fill=\"#b3d168\" fill-opacity=\"0.5\" id=\"26\" />\n
	<path d=\"M1325.0,-200.0 L1325.0,-200.0 H1350.0 V-200.0\" stroke-width=\"2\" stroke=\"#b3d168\" fill=\"#b3d168\"
		fill-opacity=\"0.5\" id=\"27\" />\n
	<path d=\"M200,-200.0 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-314.63521188291827 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />
	\n
	<path d=\"M200,-429.27042376583654 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />
	\n
	<path d=\"M200,-543.9056356487549 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-658.5408475316731 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-773.1760594145916 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-887.8112712975098 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />\n
	<path d=\"M200,-1002.4464831804282 h1200\" stroke-width=\"1\" stroke=\"gray\" fill=\"gray\" fill-opacity=\"0.5\" />
	\n
	<circle cx=\"350\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"344.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"28\">0</text>\n
	<circle cx=\"500\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"488.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"29\">15</text>\n
	<circle cx=\"650\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"644.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"30\">0</text>\n
	<circle cx=\"800\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"788.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"31\">33</text>\n
	<circle cx=\"950\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"944.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"32\">2</text>\n
	<circle cx=\"1100\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"1082.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"33\">111</text>\n
	<circle cx=\"1250\" cy=\"-200\" r=\"8\" fill=\"black\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"1238.0\"
		y=\"-153.84615384615384\" font-size=\"20.0\" id=\"34\">22</text>\n
	<circle cx=\"30\" cy=\"-58.0\" r=\"12\" fill=\"gray\" stroke-width=\"5\" stroke=\"black\" />\n<text x=\"55\"
		y=\"-50.0\" font-size=\"20.0\" id=\"35\">السعر</text>\n
	<circle cx=\"180\" cy=\"-58.0\" r=\"15\" fill=\"#b3d168\" stroke-width=\"0\" stroke=\"black\" />\n<text x=\"205\"
		y=\"-50.0\" font-size=\"20.0\" id=\"35\">الكمية</text>\n
	<circle cx=\"200\" cy=\"-200.0\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />\n<text
		x=\"57.142857142857146\" y=\"-200.0\" font-size=\"20\" id=\"35\">0.0</text>\n
	<circle cx=\"200\" cy=\"-314.63521188291827\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-314.63521188291827\" font-size=\"20\" id=\"36\">16.4</text>\n
	<circle cx=\"200\" cy=\"-429.27042376583654\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-429.27042376583654\" font-size=\"20\" id=\"37\">32.8</text>\n
	<circle cx=\"200\" cy=\"-543.9056356487549\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-543.9056356487549\" font-size=\"20\" id=\"38\">49.19999...</text>\n
	<circle cx=\"200\" cy=\"-658.5408475316731\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-658.5408475316731\" font-size=\"20\" id=\"39\">65.6</text>\n
	<circle cx=\"200\" cy=\"-773.1760594145916\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-773.1760594145916\" font-size=\"20\" id=\"40\">82.0</text>\n
	<circle cx=\"200\" cy=\"-887.8112712975098\" r=\"10\" fill=\"lightgray\" stroke-width=\"5\" stroke=\"gray\" />
	\n<text x=\"57.142857142857146\" y=\"-887.8112712975098\" font-size=\"20\" id=\"41\">98.4</text>\n</svg>
'''

string.replace('\\', '')
string.replace('\n', '')

print(string)


