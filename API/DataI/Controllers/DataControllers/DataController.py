from typing import List

from DataI.Controllers.DataControllers.DashboardsController import DashboardsController
from DataI.Controllers.DataControllers.DataSourcesController import DataSourcesController
from DataI.Controllers.DataControllers.FiltersController import FiltersController
from DataI.Controllers.DataControllers.VisualizationsController import VisualizationsController
from DataI.Controllers.FileLoaders.CSVFileLoader import CSVFileLoader
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel


class DataController():
  def __init__(self):
    self.data = DataModel([], [], [], [])

  # Don't add 1 to id here (it must be already added).
  def loadTablesFromExcelFile(self, filePath: str, greatestTableId: int):
    loader = ExcelFileLoader(filePath)
    self.data.dataSources = loader.loadFile(greatestTableId)

  # Don't add 1 to id here (it must be already added).
  def loadTableFromCSVFile(self, filePath: str, greatestTableId: int):
    loader = CSVFileLoader(filePath)
    self.data.dataSources = loader.loadFile(greatestTableId)

  def insertNewTable(self, table: TableModel):
    DataSourcesController.insertNewTable(self.data, table)

  def insertNewVisualizer(self, table: VisualizationModel):
    VisualizationsController.insertNewVisualizer(self.data, table)

  def insertNewDashboard(self, dashBoard: DashboardModel):
    DashboardsController.inserNewDashboard(self.data, dashBoard)

  def inserNewFilter(self, filter: FilterModel):
    FiltersController.inserNewFilter(self.data, filter)

  def deleteTable(self,id):
    return DataSourcesController.deleteTable(self.data,id)

  def deleteVisualizer(self,id):
    return VisualizationsController.deleteVisualizer(self.data,id)

  def deleteDashBoard(self,id):
    return DashboardsController.deleteDashBoard(self.data,id)

  def deleteFilter(self,id):
    return FiltersController.deleteFilter(self.data,id)

def getMaxIdInList(idList: List):
  max = 0
  for item in idList:
    if item.id > max:
      max = item.id
  return max

def getElementById(elementList:List, id):
  index = -1
  for single in elementList:
    if single.id == id:
      index = single.id
  return index
