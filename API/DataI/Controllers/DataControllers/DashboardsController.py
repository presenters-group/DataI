from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.DashboardModel import DashboardModel


class DashboardsController():
  @classmethod
  def inserNewDashboard(cls, data: DataModel, dashboard: DashboardModel):
    id = DataController.getMaxIdInList(data.dashboards)
    dashboard.id = id + 1
    data.dashboards.append(dashboard)


  @classmethod
  def updateDashboardById(cls, data: DataModel, dashboard: DashboardModel, id: int):
    oldDashboardIndex = DataController.getElementIndexById(data.dashboards, id)
    data.dashboards[oldDashboardIndex] = dashboard
    return data.dashboards[oldDashboardIndex]

