from numpy import double
import os
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.FemaleAndMaleChart import FemaleAndMaleChart
from DataI.Controllers.DrawControllers.FemaleInfChart import FemaleInfChart
from DataI.Controllers.DrawControllers.HealthyFoodChart import HealthyFoodChart
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Controllers.DrawControllers.LineChart import LineChart
from DataI.Controllers.DrawControllers.MultiplePieChart import MultiplePieChart
from DataI.Controllers.DrawControllers.PieChart import PieChart
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Controllers.DrawControllers.SmatPieChart import SmartPieChart

dataController = DataController()
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/home/kareem/University/Project1/web/API/Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

dataSource = dataController.data.dataSources[0]
Xcolomn = dataSource.columns[0]
dataSource.columns.pop(0)
for column in dataSource.columns:
  print(column.columnType)
char = PointChart(dataSource, double(1000), double(1000), Xcolomn, 8, "point")
chart = LineChart(dataSource, double(1000), double(1000), Xcolomn, 8, "line")
chart0 = MultiplePieChart(dataSource, Xcolomn, double(1000), double(1000), "pie")
chart1 = SmartPieChart(dataSource, Xcolomn, double(1000000), double(100), "smart")
chart2 = BarChart(dataSource, double(100), double(100), Xcolomn, 8, "BarChart")
chart4 = InfChart(dataSource, Xcolomn, double(1000000), double(100), "Human")
chart5 = FemaleInfChart(dataSource, Xcolomn, double(10), double(100), "femaInf")
chart6 = HealthyFoodChart(dataSource, Xcolomn, double(1000000), double(100), "HealthyFoodChart")
chart7 = FemaleAndMaleChart(dataSource, Xcolomn, double(1000000), double(50), "FemaleAndMaleChart")
chart3 = BoundaryLineChart(dataSource, double(1000), double(1000), Xcolomn, 8, "BoundaryLineChart")
