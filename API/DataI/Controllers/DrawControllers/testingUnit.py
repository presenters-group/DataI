from numpy import double
import os
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.LineChart import LineChart
from DataI.Controllers.DrawControllers.MultiplePieChart import MultiplePieChart
from DataI.Controllers.DrawControllers.PieChart import PieChart
from DataI.Controllers.DrawControllers.PointChart import PointChart

dataController = DataController()
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/home/kareem/University/Project1/web/API/Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

dataSource = dataController.data.dataSources[0]
Xcolomn = dataSource.columns[1]
dataSource.columns.pop(1)
for column in dataSource.columns:
  print(column.columnType)
#chart = PointChart(dataSource, double(100), double(100), Xcolomn, 8, "point")
#chart2 = BarChart(dataSource, double(100), double(100), Xcolomn, 8, "BarChart")
chart4 = MultiplePieChart(dataSource,Xcolomn ,double(100), double(100), "pie")
#chart3 = BoundaryLineChart(dataSource, double(1000), double(1000), Xcolomn, 8, "BoundaryLineChart")
