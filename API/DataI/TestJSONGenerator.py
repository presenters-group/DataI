import json

from DataI import enums
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.DashboardModel import Measurements, InDashboardFilterModel, InDashboardVisioModel, DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel
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

cells2 = [CellModel('الكمية', enums.CellType.string.value),
        CellModel(40, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(60, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(40, enums.CellType.numeric.value)
         ]

cells3 = [CellModel('النوع', enums.CellType.string.value),
        CellModel('Laptop', enums.CellType.string.value),
        CellModel('Laptop', enums.CellType.string.value),
        CellModel('Laptop', enums.CellType.string.value),
        CellModel('Mouse', enums.CellType.string.value),
        CellModel('Mouse', enums.CellType.string.value),
        CellModel('Mouse', enums.CellType.string.value),
        CellModel('Keyboard', enums.CellType.string.value),
        CellModel('Keyboard', enums.CellType.string.value),
         ]

style1 = ColumnStyleModel('#26C485', 1.0, 1.0, 'Calibri')
style2 = ColumnStyleModel('#3066BE', 1.0, 1.0, 'Calibri')
style3 = ColumnStyleModel('#DBD56E', 1.0, 1.0, 'Calibri')


column1 = ColumnModel(cells1, str(cells1[0].value), 0, style1, False)
column2 = ColumnModel(cells2, str(cells2[0].value), 1, style2, False)
column3 = ColumnModel(cells3, str(cells3[0].value), 2, style3, False)

columns = [column1, column2, column3]

#=================================================================================================================
#=================================================================================================================

properties = PropertiesModel(enums.FileType.DataI.value, 50)

aggregator = AggregationModel([], 0, False)

dataSource = TableModel(columns, 'Table1', 0, properties, aggregator, False)

#Adding a column:
#=================================================================================================================
#=================================================================================================================

newCells = [CellModel('الوزن', enums.CellType.string.value),
        CellModel(10, enums.CellType.string.value),
        CellModel(17, enums.CellType.string.value),
        CellModel(55, enums.CellType.string.value),
        CellModel(39, enums.CellType.string.value),
        CellModel(71, enums.CellType.string.value),
        CellModel(66, enums.CellType.string.value),
        CellModel(55, enums.CellType.string.value),
        CellModel(21, enums.CellType.string.value),
         ]

newStyle = ColumnStyleModel('#EBD4AE', 1.5, 0.0, 'Calibri')

newColumnId = DataController.getMaxIdInList(dataSource.columns) + 1
newColumn = ColumnModel(newCells, str(newCells[0].value), newColumnId, newStyle, False)
dataSource.columns.append(newColumn)

#=================================================================================================================
#=================================================================================================================
filter1 = dict()
filter2 = dict()
filter3 = dict()

filter1['id'] = 1
filter1['value'] = 5

filter2['id'] = 0
filter2['value'] = 'testerValue'

filter3['id'] = 2
filter3['value'] = 2142

filtersDicts = [filter1, filter2, filter3]


visualization1 = VisualizationModel(0, [0, 2], 0, 'visualization1', 0, enums.ChartTypes.BoundaryLineChart.value, filtersDicts, False)

#=================================================================================================================
#=================================================================================================================

m1 = Measurements(0.0, 0.0, 0.0, 0.0)
m2 = Measurements(1.0, 1.0, 1.0, 1.0)

inDF1 = InDashboardFilterModel(0, m1)
inDF2 = InDashboardFilterModel(1, m2)

inDV1 = InDashboardVisioModel(0, [inDF1, inDF2], m2)

dashboard1 = DashboardModel([inDV1], 'dashboard1', 0)


#=================================================================================================================
#=================================================================================================================

filterModel1 = FilterModel('filter1', 0, 0, 1, 'A', enums.FilterType.Equality.value, False)
filterModel2 = FilterModel('filter2', 1, 0, 2, 100, enums.FilterType.LessThan.value, False)
filterModel3 = FilterModel('filter3', 2, 0, 0, 11, enums.FilterType.MoreThan.value, False)

filtersList = [filterModel1, filterModel2, filterModel3]

#=================================================================================================================
#=================================================================================================================

dataSources = [dataSource]
visualizations = [visualization1]
dashboards = [dashboard1]

data = DataModel(dataSources, visualizations, dashboards, filtersList)

jsonString = json.dumps(data, indent=4, cls=ObjectEncoder, ensure_ascii=False)

fileHandler = open('Static-Data.json', 'w', encoding='utf8')

fileHandler.write(jsonString)

#=================================================================================================================
#=================================================================================================================


#=================================================================================================================
#=================================================================================================================

#deserializedData = DataModel.from_json(json.loads(jsonString))

#print(deserializedData)

#=================================================================================================================
#=================================================================================================================













