from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.LinerChart import LineChart
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Controllers.DrawControllers.chart import Chart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class ChartsFactory():

  @classmethod
  def generateCharts(cls, chartType: str, table: TableModel,
                     width: double, height: double, Xcolomn: ColumnModel, quality: double):

    if chartType == enums.ChartTypes.BasicLineChart.value:
      return LineChart(table, width, height, Xcolomn, quality)

    if chartType == enums.ChartTypes.PointChart.value:
      return PointChart(table, width, height, Xcolomn, quality)

    if chartType == enums.ChartTypes.verticalBarChart.value:
      return BarChart(table, width, height, Xcolomn, quality)



