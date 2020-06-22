import json

from django.http import HttpResponse
from DataI import enums
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.DashboardModel import Measurements, InDashboardFilterModel, InDashboardVisioModel, DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import AggregationModel, PropertiesModel, TableModel
from DataI.Models.VisualizationModel import VisualizationModel

cells1 = [CellModel('السعر', enums.CellType.string.value),
        CellModel(10, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(15, enums.CellType.numeric.value),
        CellModel(15, enums.CellType.numeric.value),
        CellModel(10, enums.CellType.numeric.value),
        CellModel(10, enums.CellType.numeric.value)
         ]


style1 = ColumnStyleModel('#26C485', 1.0, 1.0, 'Calibri')

column1 = ColumnModel(cells1, str(cells1[0].value), 10, style1, False)

col = list()
col.append(column1)
col.append(column1)

agg = AggregationModel(col, 0, False)

properties = PropertiesModel(enums.FileType.DataI.value, 50)

table = TableModel(col, 'table1', 0, properties, agg, False)

visio = VisualizationModel(0, [0, 2], 0, 'visualization1', 0, enums.ChartTypes.BoundaryLineChart.value, [0, 1], False)

filterModel = FilterModel('filter3', 0, 0, 0, 'Laptop', enums.FilterType.Equality.value, False)

m1 =  Measurements(0.0, 0.0, 0.0, 0.0)

inDF1 = InDashboardFilterModel(0, m1)

inDV1 = InDashboardVisioModel(0, [inDF1], m1)

dashboard = DashboardModel([inDV1], 'dashboard1', 0)

data = DataModel([table, table], [visio, visio], [dashboard, dashboard], [filterModel, filterModel])


def getStaticData(request):
    string = 'I am heeeeeeeeeeeeeeeeere'
    jsonString = json.dumps(data, indent=4, cls=ObjectEncoder, ensure_ascii=False)
    return HttpResponse(string + jsonString)

def modStaticData(request, question_id=1):
    oldValue = '<<' + data.visualizations[0].name + '>>'
    data.visualizations[0].name = 'ModdedVisio'
    jsonString = json.dumps(data, indent=4, cls=ObjectEncoder, ensure_ascii=False) + oldValue
    return HttpResponse(jsonString)















