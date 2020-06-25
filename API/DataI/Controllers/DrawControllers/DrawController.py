from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel
from DataI.Controllers.DataControllers import DataController

class DrawController():
  @classmethod
  def generateVisualizerTable(cls, data: DataModel, visioID: int) -> TableModel:
    columns = list()
    visioIndex = DataController.getElementIndexById(data.visualizations, visioID)
    tableIndex = data.visualizations[visioIndex].data
    for columnIndex in data.visualizations[visioIndex].usedColumns:
      columns.append(data.dataSources[tableIndex].columns[columnIndex])


