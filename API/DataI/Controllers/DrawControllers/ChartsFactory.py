from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.HumanChart import HumanChart
from DataI.Controllers.DrawControllers.MultiplePieChart import MultiplePieChart
from DataI.Controllers.DrawControllers.PieChart import PieChart
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Controllers.DrawControllers.PyramidalChart import PyramidalChart
from DataI.Controllers.DrawControllers.SmatPieChart import SmartPieChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class ChartsFactory():

  @classmethod
  def generateCharts(cls, chartType: str, table: TableModel,
                     width: double, height: double, xColomn: ColumnModel, quality: double):

    if chartType == enums.ChartTypes.BoundaryLineChart.value:
      return BoundaryLineChart(table, width, height, xColomn, quality, '')

    if chartType == enums.ChartTypes.PointChart.value:
      return PointChart(table, width, height, xColomn, quality, '')

    if chartType == enums.ChartTypes.VerticalBarChart.value:
      return BarChart(table, width, height, xColomn, quality, '')

    if chartType == enums.ChartTypes.HumanChart.value:
      return HumanChart(table.columns[0], xColomn, 'testerrr')

    if chartType == enums.ChartTypes.MultiplePieChart.value:
      return MultiplePieChart(table, xColomn, width, height, 'testerrr')

    if chartType == enums.ChartTypes.PyramidalChart.value:
      return PyramidalChart(table.columns[0], xColomn, width, height, 'testerrr')

    if chartType == enums.ChartTypes.SmartPieChart.value:
      return SmartPieChart(table.columns[0], xColomn, 'testerrr')




