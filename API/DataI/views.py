import json

from django.db import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel

import os

from DataI.forms import DocumentForm
from DataI.models import Document

dataController = DataController()
dirName = os.path.dirname(__file__)
filename = os.path.join(dirName, '../Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

# load static data:
jsonVisio = '''
{
            "name": "visualization1",
            "id": 0,
            "data": 0,
            "usedColumns": [
                0,
                2
            ],
            "xColumn": 0,
            "chart": "BoundaryLineChart",
            "filters": [
                {
                    "id": 1,
                    "value": 5
                },
                {
                    "id": 0,
                    "value": "testerValue"
                },
                {
                    "id": 2,
                    "value": 2142
                }
            ],
            "isDeleted": false
        }
'''
jsonDashboard = '''
{
            "name": "dashboard1",
            "id": 0,
            "visualizers": [
                {
                    "visualizationIndex": 0,
                    "measurements": {
                        "width": 1.0,
                        "height": 1.0,
                        "x": 1.0,
                        "y": 1.0
                    },
                    "displayedFilters": [
                        {
                            "filterIndex": 0,
                            "measurements": {
                                "width": 0.0,
                                "height": 0.0,
                                "x": 0.0,
                                "y": 0.0
                            }
                        },
                        {
                            "filterIndex": 1,
                            "measurements": {
                                "width": 1.0,
                                "height": 1.0,
                                "x": 1.0,
                                "y": 1.0
                            }
                        }
                    ]
                }
            ]
        }
'''
jsonFilters = '''
[
        {
            "name": "filter1",
            "id": 0,
            "dataSource": 0,
            "filteredColumn": 1,
            "initValue": "A",
            "type": "Equality",
            "isDeleted": false
        },
        {
            "name": "filter2",
            "id": 1,
            "dataSource": 0,
            "filteredColumn": 2,
            "initValue": 100,
            "type": "LessThan",
            "isDeleted": false
        },
        {
            "name": "filter3",
            "id": 2,
            "dataSource": 0,
            "filteredColumn": 0,
            "initValue": 11,
            "type": "MoreThan",
            "isDeleted": false
        }
    ]
'''

dataController.data.visualizations.append(VisualizationModel.from_json(json.loads(jsonVisio)))
dataController.data.dashboards.append(DashboardModel.from_json(json.loads(jsonDashboard)))
loadedJsonFilters = json.loads(jsonFilters)
for filter in loadedJsonFilters:
  dataController.data.filters.append(FilterModel.from_json(filter))


# load static data.

@csrf_exempt
def fullDataHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(dataController.data, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def dataSourcesHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(dataController.data.dataSources, indent=4, cls=ObjectEncoder, ensure_ascii=False))
  elif request.method == 'POST':
    table = TableModel.from_json(json.loads(request.body.decode()))
    dataController.insertNewTable(table)
    return HttpResponse(json.dumps(table, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def visualizersHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(dataController.data.visualizations, indent=4, cls=ObjectEncoder, ensure_ascii=False))
  elif request.method == 'POST':
    visualizer = VisualizationModel.from_json(json.loads(request.body.decode()))
    dataController.insertNewVisualizer(visualizer)
    return HttpResponse(json.dumps(visualizer, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def dashBoardsHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(dataController.data.dashboards, indent=4, cls=ObjectEncoder, ensure_ascii=False))
  elif request.method == 'POST':
    dashBoard = DashboardModel.from_json(json.loads(request.body.decode()))
    dataController.insertNewDashboard(dashBoard)
    return HttpResponse(json.dumps(dashBoard, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def filtersHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(dataController.data.filters, indent=4, cls=ObjectEncoder, ensure_ascii=False))
  elif request.method == 'POST':
    filter = FilterModel.from_json(json.loads(request.body.decode()))
    dataController.inserNewFilter(filter)
    return HttpResponse(json.dumps(filter, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def dataSourceModifier(request, id):
  if request.method == 'PUT':
    newTable = TableModel.from_json(json.loads(request.body.decode()))
    newTable = dataController.updateTableById(newTable, int(id))
    return HttpResponse(json.dumps(newTable, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def visualizerModifier(request, id):
  if request.method == 'PUT':
    newVisio = VisualizationModel.from_json(json.loads(request.body.decode()))
    newVisio = dataController.updateVisualizerById(newVisio, id)
    return HttpResponse(json.dumps(newVisio, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def dashboardModifier(request, id):
  if request.method == 'PUT':
    newDashboard = DashboardModel.from_json(json.loads(request.body.decode()))
    newDashboard = dataController.updateDashboardById(newDashboard, id)
    return HttpResponse(json.dumps(newDashboard, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def filterModifier(request, id):
  if request.method == 'PUT':
    newFilter = FilterModel.from_json(json.loads(request.body.decode()))
    newFilter = dataController.updateFilterById(newFilter, id)
    return HttpResponse(json.dumps(newFilter, indent=4, cls=ObjectEncoder, ensure_ascii=False))


@csrf_exempt
def excelUpload(request):
  #form = DocumentForm(request.POST, request.FILES)
  # if form.is_valid():
  newdoc = Document(docfile=request.FILES['file_upload'])
  try:
    newdoc.save()
  except:
    pass

  fileName = request.FILES['file_upload'].name
  dirName = os.path.dirname(__file__)
  filePath = os.path.join(dirName, '../')[1:] + fileName
  print(dataController.data.dataSources[0].id)
  dataController.loadTablesFromExcelFile(filePath, DataController.getMaxIdInList(dataController.data.dataSources) + 1)
  return HttpResponse()














