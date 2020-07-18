from typing import Dict

from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.Filters.FiltersController import FiltersController
from DataI.Models.BasicInfo import BasicDataModelInfo
from DataI.Models.DataModel import DataModel
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.TableModel import TableModel


class DashboardsController():
    @classmethod
    def insertNewDashboard(cls, data: DataModel, dashboard: DashboardModel):
        id = DataController.getMaxIdInList(data.dashboards)
        dashboard.id = id + 1
        data.dashboards.append(dashboard)

    @classmethod
    def updateDashboardById(cls, data: DataModel, dashboard: DashboardModel, id: int):
        oldDashboardIndex = DataController.getElementIndexById(data.dashboards, id)
        data.dashboards[oldDashboardIndex] = dashboard
        return data.dashboards[oldDashboardIndex]

    @classmethod
    def deleteDashBoard(cls, data: DataModel, id):
        dashBoardIndex = DataController.getElementById(data.dashboards, id)
        if dashBoardIndex != -1:
            data.dashboards[dashBoardIndex].isDeleted = True
            return data.dashboards[dashBoardIndex]
        return None

    @classmethod
    def getFilterIndex(cls, data: BasicDataModelInfo, visioId, filterId: int) -> int:
        indexCounter = 0
        for filter in data.filters:
            if filter['id'] == filterId and filter['visioId'] == visioId:
                print(filter)
                return indexCounter
            indexCounter += 1
        return -1

    @classmethod
    def getFinaleChartTable(cls, data: DataModel, dasboardId: int, visioId: int) -> TableModel:
        # Implement Aggregation Here.
        return cls.__getFilteredChartTable(data, dasboardId, visioId)

    @classmethod
    def __getFilteredChartTable(cls, data: DataModel, dasboardId: int, visioId: int) -> TableModel:
        return FiltersController.getFilteredDashboardVisio(data, dasboardId, visioId)























