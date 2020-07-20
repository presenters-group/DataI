from typing import List, Dict
from DataI import enums
from DataI.Controllers.DataControllers.DashboardsController import DashboardsController
from DataI.Controllers.DataControllers.DataSourcesController import DataSourcesController
from DataI.Controllers.DrawControllers.DrawController import DrawController
from DataI.Controllers.DataControllers.FiltersModelController import FiltersModelController
from DataI.Controllers.DataControllers.VisualizationsController import VisualizationsController
from DataI.Controllers.FileLoaders.CSVFileLoader import CSVFileLoader
from DataI.Controllers.FileLoaders.DataIFileLoader import DataIFileLoader
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader
from DataI.Controllers.Filters.FiltersController import FiltersController
from DataI.Models.BasicInfo import BasicDataModelInfo
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel


class DataController():
    def __init__(self):
        self.data = DataModel([], [], [], [])

    def loadDataIFile(self, filePath: str):
        loader = DataIFileLoader(filePath)
        self.data = loader.loadFile()

    # Don't add 1 to id here (it must be already added).
    def loadTablesFromExcelFile(self, filePath: str, greatestTableId: int):
        loader = ExcelFileLoader(filePath)
        self.data.dataSources.extend(loader.loadFile(greatestTableId))

    # Don't add 1 to id here (it must be already added).
    def loadTableFromCSVFile(self, filePath: str, greatestTableId: int):
        loader = CSVFileLoader(filePath)
        self.data.dataSources.append(loader.loadFile(greatestTableId))

    def getFinalTables(self) -> List[TableModel]:
        return DataSourcesController.getFinalTables(self.data)

    def insertNewTable(self, table: TableModel):
        DataSourcesController.insertNewTable(self.data, table)

    def updateTableById(self, table: TableModel, id: int):
        return DataSourcesController.updateTableById(self.data, table, id)

    def deleteTable(self, id):
        return DataSourcesController.deleteTable(self.data, id)

    def updateCellByCords(self, cell, tableId: int, columnId: int, cellIndex):
        return DataSourcesController.updateCellByCords(self.data, cell, tableId, columnId, cellIndex)

    def updateColumnColorById(self, color: str, tableId: int, columnId: int):
        return DataSourcesController.updateColumnColorById(self.data, color, tableId, columnId)

    def updateRowColorById(self, color: str, tableId: int, columnId: int):
        return DataSourcesController.updateRowColorById(self.data, color, tableId, columnId)

    def insertInDataSourceFilter(self, filter: Dict, tableId: int):
        targetTableIndex = DataController.getElementIndexById(self.data.dataSources, tableId)
        self.__insertInDataModelFilter(self.data.dataSources[targetTableIndex], filter)
        return FiltersController.getFilteredTable(self.data, tableId)

    def updateInDataSourceFilter(self, filter: Dict, tableId, filterId):
        targetTableIndex = DataController.getElementIndexById(self.data.dataSources, tableId)
        self.__updateInDataModelFilter(self.data.dataSources[targetTableIndex], filter, filterId)
        return FiltersController.getFilteredTable(self.data, tableId)

    def removeInDataSourceFilter(self, tableId, filterId):
        targetTableIndex = DataController.getElementIndexById(self.data.dataSources, tableId)
        value = self.__removeInDataModelFilter(self.data.dataSources[targetTableIndex], filterId)
        if value == -1:
            return -1
        return DataSourcesController.getFinalTables(self.data)[targetTableIndex]

    def insertNewVisualizer(self, table: VisualizationModel):
        return VisualizationsController.insertNewVisualizer(self.data, table)

    def updateVisualizerById(self, visio: VisualizationModel, id: int):
        return VisualizationsController.updateVisualizerById(self.data, visio, id)

    def deleteVisualizer(self, id):
        return VisualizationsController.deleteVisualizer(self.data, id)

    def insertInVisioFilter(self, filter: Dict, visioId: int):
        targetVisioIndex = DataController.getElementIndexById(self.data.visualizations, visioId)
        returnDict = self.__insertInDataModelFilter(self.data.visualizations[targetVisioIndex], filter)
        returnDict['visioId'] = visioId
        return returnDict

    def updateInVisioFilter(self, filter: Dict, visioId: int, filterId: int):
        targetVisioIndex = DataController.getElementIndexById(self.data.visualizations, visioId)
        returnDict = self.__updateInDataModelFilter(self.data.visualizations[targetVisioIndex], filter, filterId)
        returnDict['visioId'] = visioId
        return returnDict

    def removeInVisioFilter(self, visioId: int, filterId: int):
        targetVisioIndex = DataController.getElementIndexById(self.data.visualizations, visioId)
        returnDict = dict()
        returnDict['state'] = self.__removeInDataModelFilter(self.data.visualizations[targetVisioIndex], filterId)
        returnDict['visioId'] = visioId
        returnDict['filterId'] = filterId
        return returnDict

    def getChartsNames(self):
        names = [enums.ChartTypes.VerticalBarChart.value, enums.ChartTypes.BoundaryLineChart.value,
                 enums.ChartTypes.PointChart.value, enums.ChartTypes.MultiplePieChart.value,
                 enums.ChartTypes.InfChart.value, enums.ChartTypes.PyramidalChart.value,
                 enums.ChartTypes.SmartPieChart.value, enums.ChartTypes.HealthyFoodChart.value,
                 enums.ChartTypes.FemaleInfChart.value, enums.ChartTypes.FemaleAndMaleChart.value,
                 enums.ChartTypes.MapChart.value,enums.ChartTypes.LineChart.value]
        return names

    def getChart(self, visioId, width, height):
        return DrawController.getChart(self.data, visioId, width, height, VisualizationsController.getFinalTable, 0)

    def getSingleDashboardChart(self, dashboardId: int, visioId, width, height):
        return DrawController.getChart(self.data, visioId, width, height,
                                       DashboardsController.getFinaleChartTable, dashboardId)

    def insertNewDashboard(self, dashBoard: DashboardModel):
        DashboardsController.insertNewDashboard(self.data, dashBoard)

    def updateDashboardById(self, dashboard: DashboardModel, id: int):
        return DashboardsController.updateDashboardById(self.data, dashboard, id)

    def deleteDashboard(self, id):
        return DashboardsController.deleteDashBoard(self.data, id)

    def insertInDashboardFilter(self, filter: Dict, dashboardId: int):
        targetDashboardIndex = DataController.getElementIndexById(self.data.dashboards, dashboardId)
        returnDict = self.__insertInDataModelFilter(self.data.dashboards[targetDashboardIndex], filter)
        returnDict['dashboardId'] = dashboardId
        return returnDict

    def updateInDashboardFilter(self, filter: Dict, dashboardId: int, visioId: int, filterId: int):
        targetDashboardIndex = DataController.getElementIndexById(self.data.dashboards, dashboardId)
        returnDict = self.__updateInDashboardModelFilter(self.data.dashboards[targetDashboardIndex], filter,
                                                         visioId, filterId)
        returnDict['dashboardId'] = dashboardId
        return returnDict

    def removeInDashboardFilter(self, dashboardId: int, visioId: int, filterId):
        targetDashboardIndex = DataController.getElementIndexById(self.data.dashboards, dashboardId)
        returnDict = dict()
        returnDict['state'] = self.__removeInDashboardModelFilter(self.data.dashboards[targetDashboardIndex],
                                                                  visioId, filterId)
        returnDict['dashboardId'] = dashboardId
        returnDict['visioId'] = visioId
        returnDict['filterId'] = filterId
        return returnDict

    def getDashboardVisioChart(self, dashboardId: int, visioId: int) -> Dict:
        return DrawController.getDashboardVisioChart(self.data, dashboardId, visioId)

    def getAllDashboardCharts(self, dashboardId: int) -> List[Dict]:
        return DrawController.getAllDashboardCharts(self.data, dashboardId)

    def insertNewFilter(self, filter: FilterModel):
        FiltersModelController.insertNewFilter(self.data, filter)

    def updateFilterById(self, filter: FilterModel, id: int):
        return FiltersModelController.updateFilterById(self.data, filter, id)

    def deleteFilter(self, id):
        return FiltersModelController.deleteFilter(self.data, id)

    @classmethod
    def getMaxIdInList(cls, idList):
        return getMaxIdInList(idList)

    @classmethod
    def getElementIndexById(cls, list: List, id: int):
        return getElementIndexById(list, id)

    @classmethod
    def getElementIndexFromDictById(cls, list: List, id: int):
        return getElementIndexFromDictById(list, id)

    @classmethod
    def elementExists(cls, list: List, id: int) -> bool:
        return elementExists(list, id)

    @classmethod
    def __getFilterIndexFromDashboard(cls, data: BasicDataModelInfo, visioId, filterId: int) -> int:
        return DashboardsController.getFilterIndex(data, visioId, filterId)

    @classmethod
    def __insertInDataModelFilter(cls, model: BasicDataModelInfo, filter: Dict):
        model.filters.append(filter)
        return filter

    @classmethod
    def __updateInDataModelFilter(cls, model: BasicDataModelInfo, filter: Dict, filterId: int):
        inFilterIndex = DataController.getElementIndexFromDictById(model.filters, filterId)
        if inFilterIndex == -1:
            returnDict = dict()
            returnDict['state'] = -1
            return returnDict
        model.filters[inFilterIndex] = filter
        filter['state'] = 1
        return filter

    @classmethod
    def __updateInDashboardModelFilter(cls, dashboard: BasicDataModelInfo, filter: Dict, visioId: int, filterId: int):
        inFilterIndex = cls.__getFilterIndexFromDashboard(dashboard, visioId, filterId)
        if inFilterIndex == -1:
            returnDict = dict()
            returnDict['state'] = -1
            return returnDict
        dashboard.filters[inFilterIndex] = filter
        filter['state'] = 1
        return filter

    @classmethod
    def __removeInDataModelFilter(cls, model: BasicDataModelInfo, filterId: int):
        inFilterIndex = DataController.getElementIndexFromDictById(model.filters, filterId)
        if inFilterIndex == -1:
            return -1
        model.filters.pop(inFilterIndex)
        return model

    @classmethod
    def __removeInDashboardModelFilter(cls, dashboard: BasicDataModelInfo, visioId: int, filterId: int):
        inFilterIndex = cls.__getFilterIndexFromDashboard(dashboard, visioId, filterId)
        if inFilterIndex == -1:
            return -1
        dashboard.filters.pop(inFilterIndex)
        return 1


def getMaxIdInList(idList):
    max = 0
    for item in idList:
        if item.id > max:
            max = item.id
    return max


def getElementById(elementsList: List, id):
    index = -1
    for element in elementsList:
        if element.id == id:
            index = element.id
    return index


def getElementIndexById(list: List, id: int):
    indexCounter = 0
    for element in list:
        if element.id == id:
            return indexCounter
        indexCounter += 1
    return -1


def getElementIndexFromDictById(list: List, id: int):
    indexCounter = 0
    for element in list:
        if element['id'] == id:
            return indexCounter
        indexCounter += 1
    return -1


def elementExists(list: List, id: int) -> bool:
    for element in list:
        if element.id == id:
            return True
    return False
