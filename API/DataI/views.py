import json
import os

from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from DataI.Controllers.DataControllers.DataController import DataController
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel
from DataI.models import Document

dataController = DataController()
dirName = os.path.dirname(__file__)
filename = os.path.join(dirName, '../Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

# ================================ load static data ================================:


jsonVisio1 = '''
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
            "chart": "BoundaryLineChart
            "filters": [
            ],
            "isDeleted": false
}
'''
jsonVisio2 = '''
{
            "name": "visualization2",
            "id": 1,
            "data": 0,
            "usedColumns": [
                0,
                1,
                2
            ],
            "xColumn": 0,
            "chart": "VerticalBarChart",
            "filters": [
            ],
            "isDeleted": false
}
'''

jsonDashboard = '''
{
    "name": "dashboard1",
    "id": 0,
    "isDeleted": false,
    "visualizers": [
        {
            "visualizationId": 0,
            "measurements": {
                "width": 100.0,
                "height": 100.0,
                "x": 50.0,
                "y": 60.0
            }
        }
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
    "filters": [
        {
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
        }
    ]
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
            "filteredColumn": 0,
            "initValue": 11,
            "type": "<",
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

# dataController.data.dataSources[0].filters = [filter1, filter2]
# dataController.data.dataSources[1].filters = [filter3]
# dataController.data.visualizations[0].filters = [filter1]


# ================================ load static data ================================.


@csrf_exempt
def fullDataHandler(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(dataController.data, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def dataSourcesHandler(request):
    if request.method == 'GET':
        fullTables = dataController.getFinalTables()
        return HttpResponse(
            json.dumps(fullTables, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    elif request.method == 'POST':
        table = TableModel.from_json(json.loads(request.body.decode()))
        dataController.insertNewTable(table)
        return HttpResponse(json.dumps(table, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def dataSourceModifier(request, id):
    if request.method == 'PUT':
        newTable = TableModel.from_json(json.loads(request.body.decode()))
        newTable = dataController.updateTableById(newTable, int(id))
        return HttpResponse(json.dumps(newTable, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    elif request.method == 'DELETE':
        table = dataController.deleteTable(id)
        return HttpResponse(json.dumps(table, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def cellModifier(request, tableId, columnId, cellIndex):
    if request.method == 'PUT':
        newCell = json.loads(request.body.decode()).get('cellValue')
        newCell = dataController.updateCellByCords(newCell, tableId, columnId, cellIndex)
        returnDict = dict()
        returnDict['cellValue'] = newCell.value
        returnDict['tableID'] = tableId
        returnDict['columnId'] = columnId
        returnDict['cellIndex'] = cellIndex
        return HttpResponse(json.dumps(returnDict, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def columnColorModifier(request, tableId, columnId):
    if request.method == 'PUT':
        newColor = json.loads(request.body.decode()).get('color')
        table = dataController.updateColumnColorById(newColor, tableId, columnId)
        return HttpResponse(json.dumps(table, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def rowColorModifier(request, tableId, rowId):
    if request.method == 'PUT':
        newColor = json.loads(request.body.decode()).get('color')
        table = dataController.updateRowColorById(newColor, tableId, rowId)
        return HttpResponse(json.dumps(table, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def insertInDataSourceFilter(request, tableId):
    if request.method == 'PUT':
        filter = json.loads(request.body.decode())
        returnTable = dataController.insertInDataSourceFilter(filter, tableId)
        return HttpResponse(json.dumps(returnTable, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def updateInDataSourceFilter(request, tableId, filterId):
    if request.method == 'PUT':
        filter = json.loads(request.body.decode())
        returnTable = dataController.updateInDataSourceFilter(filter, tableId, filterId)
        if returnTable == -1:
            return HttpResponseNotFound('Filter not found.')
        return HttpResponse(json.dumps(returnTable, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def removeInDataSourceFilter(request, tableId, filterId):
    if request.method == 'PUT':
        returnValue = dataController.removeInDataSourceFilter(tableId, filterId)
        if returnValue == -1:
            return HttpResponseNotFound('Filter not found.')
        return HttpResponse(json.dumps(returnValue, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def visualizersHandler(request):
    if request.method == 'GET':
        return HttpResponse(
            json.dumps(dataController.data.visualizations, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    elif request.method == 'POST':
        visualizer = VisualizationModel.from_json(json.loads(request.body.decode()))
        dataController.insertNewVisualizer(visualizer)
        return HttpResponse(json.dumps(visualizer, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def visualizerModifier(request, id):
    if request.method == 'PUT':
        newVisio = VisualizationModel.from_json(json.loads(request.body.decode()))
        newVisio = dataController.updateVisualizerById(newVisio, id)
        return HttpResponse(json.dumps(newVisio, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    elif request.method == 'DELETE':
        visualizer = dataController.deleteVisualizer(id)
        return HttpResponse(json.dumps(visualizer, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def insertInVisioFilter(request, visioId):
    if request.method == 'PUT':
        filter = json.loads(request.body.decode())
        returnFilter = dataController.insertInVisioFilter(filter, visioId)
        return HttpResponse(json.dumps(returnFilter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def updateInVisioFilter(request, visioId, filterId):
    if request.method == 'PUT':
        filter = json.loads(request.body.decode())
        returnFilter = dataController.updateInVisioFilter(filter, visioId, filterId)
        print(returnFilter['state'])
        if returnFilter['state'] == -1:
            return HttpResponseNotFound('Filter not found.')
        return HttpResponse(json.dumps(returnFilter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def removeInVisioFilter(request, visioId, filterId):
    if request.method == 'PUT':
        returnValue = dataController.removeInVisioFilter(visioId, filterId)
        if returnValue['state'] == -1:
            return HttpResponseNotFound('Filter not found.')
        return HttpResponse(json.dumps(returnValue, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def getChartsNames(request):
    if request.method == 'GET':
        chartsNames = dataController.getChartsNames()
        namesDict = dict()
        namesDict['chartsNames'] = chartsNames
        return HttpResponse(json.dumps(namesDict, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def getChartSVG(request):
    if request.method == 'PUT':
        visioInfo = json.loads(request.body.decode())
        visualizerId = visioInfo.get('visualizerId')
        width = visioInfo.get('width')
        height = visioInfo.get('height')
        chart = dataController.getChart(visualizerId, width, height)
        return HttpResponse(json.dumps(chart, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def dashBoardsHandler(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(dataController.data.dashboards, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    elif request.method == 'POST':
        dashBoard = DashboardModel.from_json(json.loads(request.body.decode()))
        dataController.insertNewDashboard(dashBoard)
        return HttpResponse(json.dumps(dashBoard, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def dashboardModifier(request, id):
    if request.method == 'PUT':
        newDashboard = DashboardModel.from_json(json.loads(request.body.decode()))
        newDashboard = dataController.updateDashboardById(newDashboard, id)
        return HttpResponse(json.dumps(newDashboard, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    if request.method == 'DELETE':
        dashBoard = dataController.deleteDashboard(id)
        return HttpResponse(json.dumps(dashBoard, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def insertInDashboardFilter(request, dashboardId):
    if request.method == 'PUT':
        filter = json.loads(request.body.decode())
        returnFilter = dataController.insertInDashboardFilter(filter, dashboardId)
        return HttpResponse(json.dumps(returnFilter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def updateInDashboardFilter(request, dashboardId, visioId, filterId):
    if request.method == 'PUT':
        filter = json.loads(request.body.decode())
        returnFilter = dataController.updateInDashboardFilter(filter, dashboardId, visioId, filterId)
        if returnFilter['state'] == -1:
            return HttpResponseNotFound('Filter not found.')
        return HttpResponse(json.dumps(returnFilter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def removeInDashboardFilter(request, dashboardId, visioId, filterId):
    if request.method == 'PUT':
        returnValue = dataController.removeInDashboardFilter(dashboardId, visioId, filterId)
        if returnValue['state'] == -1:
            return HttpResponseNotFound('Filter not found.')
        return HttpResponse(json.dumps(returnValue, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def filtersHandler(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(dataController.data.filters, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    elif request.method == 'POST':
        filter = FilterModel.from_json(json.loads(request.body.decode()))
        dataController.insertNewFilter(filter)
        return HttpResponse(json.dumps(filter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def filterModifier(request, id):
    if request.method == 'PUT':
        newFilter = FilterModel.from_json(json.loads(request.body.decode()))
        newFilter = dataController.updateFilterById(newFilter, id)
        return HttpResponse(json.dumps(newFilter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    if request.method == 'DELETE':
        filter = dataController.deleteFilter(id)
        return HttpResponse(json.dumps(filter, indent=4, cls=ObjectEncoder, ensure_ascii=False))
    else:
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))


@csrf_exempt
def excelUpload(request):
    if request.method != 'PUT':
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))

    newdoc = Document(docfile=request.FILES['file_upload'])
    try:
        newdoc.save()
    except:
        pass

    fileName = request.FILES['file_upload'].name
    projectPath = os.path.dirname(__file__)
    print('project path: ' + projectPath)
    filePath = projectPath.replace('/DataI', '') + '/media/uploads/' + fileName
    print(filePath)
    dataController.loadTablesFromExcelFile(filePath, DataController.getMaxIdInList(dataController.data.dataSources) + 1)
    return HttpResponse()


@csrf_exempt
def csvUpload(request):
    if request.method != 'PUT':
        return HttpResponseNotFound('No such request({} <{}>) is available'.format(request.path, request.method))

    newdoc = Document(docfile=request.FILES['file_upload'])
    try:
        newdoc.save()
    except:
        pass

    fileName = request.FILES['file_upload'].name
    projectPath = os.path.dirname(__file__)
    print('project path: ' + projectPath)
    filePath = (os.path.join(projectPath.replace('/DataI', '')) + '/media/uploads/') + fileName
    print(filePath)
    dataController.loadTableFromCSVFile(filePath, DataController.getMaxIdInList(dataController.data.dataSources) + 1)
    return HttpResponse()
