from numpy import double, long

from Charts.PointChart import PointChart
from Charts.LinerChart import LinertChart
from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel

cells1 = [CellModel('السعر', enums.CellType.string.value),
        CellModel(-10, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(0, enums.CellType.numeric.value),
        CellModel(-5, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(-8, enums.CellType.numeric.value),
        CellModel(-8, enums.CellType.numeric.value),
        CellModel(-8, enums.CellType.numeric.value),
        CellModel(-8, enums.CellType.numeric.value),
        CellModel(-9, enums.CellType.numeric.value),
        CellModel(-1, enums.CellType.numeric.value)
         ]

cells2 = [CellModel('الكمية', enums.CellType.string.value),
        CellModel(-0.5, enums.CellType.numeric.value),
        CellModel(-3, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(-3.555, enums.CellType.numeric.value),
        CellModel(-1, enums.CellType.numeric.value),
        CellModel(-1, enums.CellType.numeric.value),
        CellModel(-1, enums.CellType.numeric.value),
        CellModel(-1, enums.CellType.numeric.value),
        CellModel(3.5, enums.CellType.numeric.value),
        CellModel(-3, enums.CellType.numeric.value),
        CellModel(-2, enums.CellType.numeric.value)
         ]

cells3 = [CellModel('الحجم', enums.CellType.string.value),
        CellModel('-30000268400000000', enums.CellType.numeric.value),
        CellModel('80', enums.CellType.numeric.value),
        CellModel('15', enums.CellType.numeric.value),
        CellModel('-65', enums.CellType.numeric.value),
        CellModel('15',enums.CellType.numeric.value),
        CellModel('5', enums.CellType.numeric.value),
        CellModel('5', enums.CellType.numeric.value),
        CellModel('5', enums.CellType.numeric.value),
        CellModel('5', enums.CellType.numeric.value),
        CellModel('8', enums.CellType.numeric.value),
        CellModel('99', enums.CellType.numeric.value),
         ]

style1 = ColumnStyleModel('#26C485', 1.0, 1.0, 'Calibri')
style2 = ColumnStyleModel('#3066BE', 1.0, 1.0, 'Calibri')
style3 = ColumnStyleModel('#DBD56E', 1.0, 1.0, 'Calibri')


column1 = ColumnModel(cells1, cells1[0].value, 0, style1, False)
column2 = ColumnModel(cells2, cells2[0].value, 1, style2, False)
column3 = ColumnModel(cells3, cells3[0].value, 2, style3, False)

columns = [column1, column2, column3]

#=================================================================================================================
#=================================================================================================================

properties = PropertiesModel(enums.FileType.DataI.value, 50)

aggregator = AggregationModel([], 0, False)

testdatasource = TableModel(columns, 'Table1', 0, properties, aggregator, False)

#=================================================================================================================
#=================================================================================================================



import drawSvg as draw


dataSource = testdatasource
Xcolomn =dataSource.columns[2]
chart = PointChart(dataSource,double(1000),double(1000),Xcolomn,8,"point")
chart2 = LinertChart(dataSource,double(1000),double(1000),Xcolomn,8,"Line")
print(chart.lsitOfIndexing)

