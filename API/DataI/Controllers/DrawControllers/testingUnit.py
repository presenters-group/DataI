from numpy import double
import os
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.LineChart import LineChart
from DataI.Controllers.DrawControllers.PointChart import PointChart

dataController = DataController()
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/home/kareem/University/Project1/web/API/Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)


<<<<<<< HEAD
dataSource = dataController.data.dataSources[0]
Xcolomn = dataSource.columns[1]
dataSource.columns.pop(1)
for column in dataSource.columns:
  print(column.columnType)
chart = PointChart(dataSource, double(100), double(100), Xcolomn, 8, "point")
chart2 = BarChart(dataSource, double(100), double(500), Xcolomn, 8, "BarChart")
chart3 = BoundaryLineChart(dataSource, double(1000), double(1000), Xcolomn, 8, "BoundaryLineChart")
=======
style1 = ColumnStyleModel('#26C485', 1.0, 1.0, 'Calibri')
style2 = ColumnStyleModel('#3066BE', 1.0, 1.0, 'Calibri')
style3 = ColumnStyleModel('#DBD56E', 1.0, 1.0, 'Calibri')

column1 = ColumnModel(cells1, cells1[0].value, 0, False)
column2 = ColumnModel(cells2, cells2[0].value, 1, False)
column3 = ColumnModel(cells3, cells3[0].value, 2, False)

columns = [column1, column2, column3]

# =================================================================================================================
# =================================================================================================================

properties = PropertiesModel(enums.FileType.DataI.value, 50)

aggregator = AggregationModel([], 0, False)

testdatasource = TableModel(columns, 'Table1', 0, properties, aggregator, [], False)

# =================================================================================================================
# =================================================================================================================


dataSource = testdatasource
Xcolomn = dataSource.columns[2]
dataSource.columnsColors = ['']
chart = PointChart(dataSource, double(1000), double(1000), Xcolomn, 8, "point")
chart2 = LineChart(dataSource, double(1000), double(1000), Xcolomn, 8, "Line")
print(chart.listOfIndexing)
>>>>>>> 63c24a2d03022ca5d5883c7cc72406cff8a1cd84
