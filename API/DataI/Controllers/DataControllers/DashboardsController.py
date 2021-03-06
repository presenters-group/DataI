from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.Filters import FiltersController
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
    def getFilteredChartTable(cls, data: DataModel, dasboardId: int, visioId: int) -> TableModel:
        return FiltersController.getFilteredDashboardVisio(data, dasboardId, visioId)



# def insertNewDashboard(data: DataModel, dashBoard: DashboardModel):
#     DashboardsController.insertNewDashboard(data, dashBoard)
#
#
# def updateDashboardById(data: DataModel, dashboard: DashboardModel, id: int):
#     return DashboardsController.updateDashboardById(data, dashboard, id)
#
# def deleteDashBoard(data: DataModel, id):
#     return DashboardsController.deleteDashBoard(data, id)
#
#
# def getFilterIndex(data: BasicDataModelInfo, visioId, filterId: int) -> int:
#     return DashboardsController.getFilterIndex(data, visioId, filterId)
#
# def getFinaleChartTable(data: DataModel, dasboardId: int, visioId: int) -> TableModel:
#     return DashboardsController.getFinaleChartTable(data, dasboardId, visioId)

















