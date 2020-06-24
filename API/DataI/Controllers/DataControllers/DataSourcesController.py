from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel


class DataSourcesController():
  @classmethod
  def insertNewTable(self, data: DataModel, table: TableModel):
    id = DataController.getMaxIdInList(data.dataSources)
    table.id = id + 1
    data.dataSources.append(table)
