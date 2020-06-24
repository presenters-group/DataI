import json
from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel


class DataSourcesController():
  @classmethod
  def insertNewTable(self, data: DataModel, table: TableModel):
    id = DataController.getMaxIdInList(data.dataSources)
    table.id = id + 1
    data.dataSources.append(table)
  @classmethod
  def deleteTable(self,data:DataModel,id):
    elementIndex = DataController.getElementById(data.dataSources, id)
    if elementIndex != -1:
      data.dataSources[elementIndex].isDeleted = True
      return data.dataSources[elementIndex]
    return None

  @classmethod
  def updateTableById(self, data: DataModel, table: TableModel, id: int):
    oldTableIndex = DataController.getElementIndexById(data.dataSources, id)
    data.dataSources[oldTableIndex] = table
    return data.dataSources[oldTableIndex]

