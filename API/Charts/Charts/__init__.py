from numpy import double

from Charts.Charts.HumanChart import HumanChart
from Charts.Charts.PieChart import PieChart
from Charts.Charts.MultiplePieChart import MultiplePieChart
from Charts.Charts.PointChart import PointChart
from Charts.Charts.LineChart import LineChart
from Charts.Charts.BarChart import BarChart
from Charts.Charts.PyramidalChart import PyramidalChart
from Charts.Charts.SmatPieChart import SmartPieChart
from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel



cells2 = [CellModel('table', enums.CellType.string.value),
        CellModel('300', enums.CellType.numeric.value),
        CellModel(30, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(10, enums.CellType.numeric.value),
        CellModel(7, enums.CellType.numeric.value),
        CellModel(38, enums.CellType.numeric.value),
        CellModel(83, enums.CellType.numeric.value)
         ]
cells3 = [CellModel('size', enums.CellType.string.value),
        CellModel('Huge', enums.CellType.string.value),
        CellModel('Tiny', enums.CellType.string.value),
        CellModel('Large', enums.CellType.string.value),
        CellModel('Small', enums.CellType.string.value),
        CellModel('Extra small', enums.CellType.string.value),
        CellModel('Extra Large', enums.CellType.string.value),
        CellModel('Middle', enums.CellType.string.value)
         ]
cells4 = [CellModel('IT', enums.CellType.string.value),
        CellModel(39, enums.CellType.numeric.value),
        CellModel(80, enums.CellType.numeric.value),
        CellModel(37, enums.CellType.numeric.value),
        CellModel(96, enums.CellType.numeric.value),
        CellModel(102, enums.CellType.numeric.value),
        CellModel(90, enums.CellType.numeric.value),
        CellModel(30, enums.CellType.numeric.value)
         ]
cells5 = [CellModel('Kareem', enums.CellType.string.value),
        CellModel(13, enums.CellType.numeric.value),
        CellModel(-93, enums.CellType.numeric.value),
        CellModel(83, enums.CellType.numeric.value),
        CellModel(37, enums.CellType.numeric.value),
        CellModel(38, enums.CellType.numeric.value),
        CellModel(39, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(37, enums.CellType.numeric.value)
         ]
cells6 = [CellModel('size', enums.CellType.string.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value),
        CellModel(3, enums.CellType.numeric.value)
         ]
style1 = ColumnStyleModel('#26C485', 1.0, 1.0, 'Calibri')
style2 = ColumnStyleModel('#3066BE', 1.0, 1.0, 'Calibri')
style3 = ColumnStyleModel('#DBD56E', 1.0, 1.0, 'Calibri')
style4 = ColumnStyleModel('#D0D51E', 1.0, 1.0, 'Calibri')
style5 = ColumnStyleModel('#D8876E', 1.0, 1.0, 'Calibri')
style6 = ColumnStyleModel('#DfD160', 1.0, 1.0, 'Calibri')


column2 = ColumnModel(cells2, str(cells2[0].value), 2, style2, False)
column3 = ColumnModel(cells3, str(cells3[0].value), 3, style3, False)
column4 = ColumnModel(cells4, str(cells4[0].value), 4, style4, False)
column5 = ColumnModel(cells5, str(cells5[0].value), 5, style5, False)
column6 = ColumnModel(cells6, str(cells6[0].value), 6, style6, False)

columns = [column2,column4,column5,column4,column5,column4]

#=================================================================================================================
#=================================================================================================================

properties = PropertiesModel(enums.FileType.DataI.value, 50)

aggregator = AggregationModel([], 0, False)

testdatasource = TableModel(columns, 'Table1', 0, properties, aggregator, False)

#=================================================================================================================
#===============================================================
dataSource = testdatasource
Xcolomn = column3
for column in dataSource.columns:
  print("i=",column.id,"type",column.columnType)
#chart4 = SmartPieChart(dataSource.columns[0],dataSource.columns[1],"l")
#chart8 = HumanChart(dataSource.columns[0],dataSource.columns[1],"Human")
#chart5 = PieChart(dataSource.columns[0],dataSource.columns[1],1000,1000,"pie")
#chart = MultiplePieChart(dataSource, Xcolomn, 1000, 1000, "pied")
#chart9 = BarChart(dataSource, 1400, 1000, Xcolomn, 8, "test")
chartl = LineChart(dataSource, 500, 500, Xcolomn, 10, "t")
chart9 = PointChart(dataSource, 200, 20, Xcolomn, 10, "ss")

chart10 = SmartPieChart(dataSource.columns[0],dataSource.columns[1],"Smartpie")
ss = SmartPieChart(dataSource.columns[0],dataSource.columns[1],"Smartpie")

print("____________________________________________________________")
