from numpy import double
import os
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.CustomChart import CustomChart
from DataI.Controllers.DrawControllers.FemaleAndMaleChart import FemaleAndMaleChart
from DataI.Controllers.DrawControllers.FemaleInfChart import FemaleInfChart
from DataI.Controllers.DrawControllers.HealthyFoodChart import HealthyFoodChart
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Controllers.DrawControllers.LineChart import LineChart
from DataI.Controllers.DrawControllers.MapChart import MapChart
from DataI.Controllers.DrawControllers.MultiplePieChart import MultiplePieChart
from DataI.Controllers.DrawControllers.PieChart import PieChart
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Controllers.DrawControllers.SmatPieChart import SmartPieChart

# from svg.path import parse_path
# with open("/home/kareem/m.svg", "r") as myfile:
#   data = myfile.readlines()
# print(data)

from xml.dom import minidom
doc = minidom.parse("/home/kareem/m.svg")
path_id = [path.getAttribute('id') for path
                in doc.getElementsByTagName('path')]
path_data = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
doc.unlink()
i=0
# for path,id in zip(path_data,path_id):
#   i+=1
#   print(i," ",id,":",path)

# svg_dom = minidom.parseString("/home/kareem/m.svg")
#
# path_strings = [path.getAttribute('d') for path in svg_dom.getElementsByTagName('path')]

# for path_string in path_strings:
#     path_data = parse_path(path_string)

# returns first occurrence of Substring


dataController = DataController()
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/home/kareem/University/Project1/web/API/Test.xlsx')

dataController.loadTablesFromExcelFile(filename, 0)

dataSource = dataController.data.dataSources[0]
# for column in dataSource.columns:
#   print(column.name)
#   print(column.columnType)
Xcolomn = dataSource.columns[3]
print(Xcolomn.name)
dataSource.columns.pop(3)
# char = PointChart(dataSource, double(1000), double(1000), Xcolomn, 8,True, "point")
# chart = LineChart(dataSource, double(1000), double(1000), Xcolomn, 8, True, "line")
# chart0 = MultiplePieChart(dataSource, Xcolomn, double(1000), double(1000), True, "pie")
chart1 = SmartPieChart(dataSource, Xcolomn, double(2000), double(1000), True, "smart")
# chart2 = InfChart(dataSource, Xcolomn, double(1000), double(1000), True, "Inf")
# chart2 = BarChart(dataSource, double(1000), double(1000), Xcolomn, 8, True, "BarChart")
# chart4 = MapChart(dataSource, Xcolomn, double(1000), double(1000), True, "mtest")

# chart5 = FemaleInfChart(dataSource, Xcolomn, double(10), double(100), True, "femaInf")
# chart6 = HealthyFoodChart(dataSource, Xcolomn, double(1000000), double(100), True, "HealthyFoodChart")

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# dir =str(ROOT_DIR) + "/T.svg"
# chart_6 = CustomChart(dataSource, Xcolomn, double(1000000), double(100), False, "CustomChart",dir)
# chart7 = FemaleAndMaleChart(dataSource, Xcolomn, double(1000000), double(50), True, "FemaleAndMaleChart")
# chart3 = BoundaryLineChart(dataSource, double(1000), double(1000), Xcolomn, 8, True, "BoundaryLineChart")
