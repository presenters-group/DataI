from numpy import double

from DataI.Controllers.DrawControllers.ChartsFactory import ChartsFactory
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

    returnTable = TableModel(columns,
                             data.dataSources[tableIndex].name,
                             data.dataSources[tableIndex].id,
                             data.dataSources[tableIndex].properties,
                             data.dataSources[tableIndex].aggregator,
                             data.dataSources[tableIndex].isDeleted)

    return returnTable


  @classmethod
  def getSVGString(cls, data: DataModel, visioID: int, width: double, height: double) -> str:
    visioIndex = DataController.getElementIndexById(data.visualizations, visioID)
    visualizer = data.visualizations[visioIndex]
    drawTable = cls.generateVisualizerTable(data, visioID)
    xColumn = cls.__seperateXColumn(drawTable, visualizer.xColumn)
    drawer = ChartsFactory.generateCharts(visualizer.chart, drawTable, width, height, xColumn, double(8.0))
    return drawer.SVG

  @classmethod
  def __seperateXColumn(cls, table: TableModel, xColumnId: int):
    xColumnIndex = DataController.getElementIndexById(table.columns, xColumnId)
    XColumn = table.columns[xColumnIndex]
    table.columns.remove(XColumn)
    return XColumn









