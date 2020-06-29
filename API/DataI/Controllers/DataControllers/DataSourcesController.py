import json

from DataI import enums
from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel


class DataSourcesController():
  @classmethod
  def insertNewTable(cls, data: DataModel, table: TableModel):
    id = DataController.getMaxIdInList(data.dataSources)
    table.id = id + 1
    data.dataSources.append(table)

  @classmethod
  def updateTableById(cls, data: DataModel, table: TableModel, id: int):
    oldTableIndex = DataController.getElementIndexById(data.dataSources, id)
    data.dataSources[oldTableIndex] = table
    return data.dataSources[oldTableIndex]

  @classmethod
  def updateCellByCords(cls, data: DataModel,cell, tableId: int, columnId: int, cellIndex):
    targetTableIndex = DataController.getElementIndexById(data.dataSources, tableId)
    targetColumnIndex = DataController.getElementIndexById(data.dataSources[targetTableIndex].columns, columnId)
    data.dataSources[targetTableIndex].columns[targetColumnIndex].cells[cellIndex].value = cell
    data.dataSources[targetTableIndex].columns[targetColumnIndex].cells[cellIndex].type = cls.__getCellType(cell)
    return data.dataSources[targetTableIndex].columns[targetColumnIndex].cells[cellIndex]



  @classmethod
  def deleteTable(cls, data: DataModel, id: int):
    elementIndex = DataController.getElementById(data.dataSources, id)
    if elementIndex != -1:
      data.dataSources[elementIndex].isDeleted = True
      return data.dataSources[elementIndex]
    return None

  @classmethod
  def __getCellType(cls, cell):
    if type(cell) is str:
      return enums.CellType.string.value
    else:
      return enums.CellType.numeric.value

