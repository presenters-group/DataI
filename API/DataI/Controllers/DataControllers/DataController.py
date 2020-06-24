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

  def updateTableById(self, table: TableModel, id: int):
    return DataSourcesController.updateTableById(self.data, table, id)

  def updateVisualizerById(self, visio: VisualizationModel, id: int):
    return VisualizationsController.updateVisualizerById(self.data, visio, id)

  def updateDashboardById(self, dashboard: DashboardModel, id: int):
    return DashboardsController.updateDashboardById(self.data, dashboard, id)

  def updateFilterById(self, filter: FilterModel, id: int):
    return FiltersController.updateFilterById(self.data, filter, id)



def getMaxIdInList(idList: List):
  max = 0
  for item in idList:
    if item.id > max:
      max = item.id
  return max

def getElementIndexById(list: List, id: int):
  indexCounter = 0
  for element in list:
    if element.id == id:
      return indexCounter
    indexCounter += 1
