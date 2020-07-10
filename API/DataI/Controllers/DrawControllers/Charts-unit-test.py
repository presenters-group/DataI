from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.DrawControllers.LineChart import LineChart
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader

dataController = DataController()

loader = ExcelFileLoader('/home/kareem/University/Project1/web/API/Test.xlsx')
dataController.data.dataSources = loader.loadFile(0)
dataSource = dataController.data.dataSources[0]
xColumn = dataSource.columns[0]
dataSource.columns.pop(0)
print(xColumn.cells)
chart = LineChart(dataSource, 1000, 1000, xColumn, 8, "FromFileTest")
