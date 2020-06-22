import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel

jsonString = '''
  {
    "dataSources": [
        {
            "name": "Table1",
            "id": 0,
            "columns": [
                {
                    "name": "السعر",
                    "id": 500,
                    "cells": [
                        {
                            "value": "السعر",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 15,
                            "type": "numeric"
                        },
                        {
                            "value": 15,
                            "type": "numeric"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        }
                    ],
                    "style": {
                        "color": "#26C485",
                        "lineWeight": 1.0,
                        "pointWeight": 1.0,
                        "font": "Calibri"
                    },
                    "columnType": "Measures",
                    "valueCategories": [
                        {
                            "value": "السعر",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 15,
                            "type": "numeric"
                        }
                    ],
                    "isDeleted": false
                },
                {
                    "name": "الكمية",
                    "id": 40,
                    "cells": [
                        {
                            "value": "الكمية",
                            "type": "string"
                        },
                        {
                            "value": 40,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 60,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 40,
                            "type": "numeric"
                        }
                    ],
                    "style": {
                        "color": "#3066BE",
                        "lineWeight": 1.0,
                        "pointWeight": 1.0,
                        "font": "Calibri"
                    },
                    "columnType": "Measures",
                    "valueCategories": [
                        {
                            "value": "الكمية",
                            "type": "string"
                        },
                        {
                            "value": 40,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 60,
                            "type": "numeric"
                        }
                    ],
                    "isDeleted": false
                },
                {
                    "name": "النوع",
                    "id": 359,
                    "cells": [
                        {
                            "value": "النوع",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Keyboard",
                            "type": "string"
                        },
                        {
                            "value": "Keyboard",
                            "type": "string"
                        }
                    ],
                    "style": {
                        "color": "#DBD56E",
                        "lineWeight": 1.0,
                        "pointWeight": 1.0,
                        "font": "Calibri"
                    },
                    "columnType": "Dimensions",
                    "valueCategories": [
                        {
                            "value": "النوع",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Keyboard",
                            "type": "string"
                        }
                    ],
                    "isDeleted": false
                },
                {
                    "name": "الوزن",
                    "id": 501,
                    "cells": [
                        {
                            "value": "الوزن",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "string"
                        },
                        {
                            "value": 17,
                            "type": "string"
                        },
                        {
                            "value": 55,
                            "type": "string"
                        },
                        {
                            "value": 39,
                            "type": "string"
                        },
                        {
                            "value": 71,
                            "type": "string"
                        },
                        {
                            "value": 66,
                            "type": "string"
                        },
                        {
                            "value": 55,
                            "type": "string"
                        },
                        {
                            "value": 21,
                            "type": "string"
                        }
                    ],
                    "style": {
                        "color": "#EBD4AE",
                        "lineWeight": 1.5,
                        "pointWeight": 0.0,
                        "font": "Calibri"
                    },
                    "columnType": "Measures",
                    "valueCategories": [
                        {
                            "value": "الوزن",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "string"
                        },
                        {
                            "value": 17,
                            "type": "string"
                        },
                        {
                            "value": 55,
                            "type": "string"
                        },
                        {
                            "value": 39,
                            "type": "string"
                        },
                        {
                            "value": 71,
                            "type": "string"
                        },
                        {
                            "value": 66,
                            "type": "string"
                        },
                        {
                            "value": 21,
                            "type": "string"
                        }
                    ],
                    "isDeleted": false
                }
            ],
            "columnsVisibility": [
                true,
                true,
                true
            ],
            "rowsVisibility": [
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "properties": {
                "sourceFileType": "DataI",
                "zoomValue": 50
            },
            "aggregator": null,
            "isDeleted": false
        }
    ],
    "visualizations": [
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
    ],
    "dashboards": [
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
    ],
    "filters": [
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
            "id": 500,
            "dataSource": 0,
            "filteredColumn": 0,
            "initValue": 11,
            "type": "MoreThan",
            "isDeleted": false
        }
    ]
}
'''

data = DataModel.from_json(json.loads(jsonString))

def initializeApp(data: DataModel):
  loader = ExcelFileLoader('file:///home/allonios/FullEnd/API/Test.xlsx')
  data.dataSources = loader.loadFile(0)

#initializeApp(data)


def fullDataHandler(request):
  if request.method == 'GET':
    return
  elif request.method == 'POST':
    data.from_json(postFullData(request))

def postFullData(request):
  pass


@csrf_exempt
def dataSourcesHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(data.dataSources, indent= 4, cls= ObjectEncoder, ensure_ascii= False))
  elif request.method == 'POST':
    data.dataSources.clear()
    jsonDataSources = json.loads(request.body.decode()).get('dataSources')
    for jsonTable in jsonDataSources:
      data.dataSources.append(TableModel.from_json(jsonTable))

    print(data.dataSources[0].columns[0].cells[0].value)

    return HttpResponse()



def visualizersHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(data.visualizations, indent= 4, cls= ObjectEncoder, ensure_ascii= False))
  elif request.method == 'POST':
    postVisualizers(request)

def postVisualizers(request):
  pass



def dashBoardsHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(data.dashboards, indent= 4, cls= ObjectEncoder, ensure_ascii= False))
  elif request.method == 'POST':
    postDashboards(request)

def postDashboards(request):
  pass



def filtersHandler(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(data.filters, indent= 4, cls= ObjectEncoder, ensure_ascii= False))
  elif request.method == 'POST':
    postFilters(request)

def postFilters(request):
  pass






















