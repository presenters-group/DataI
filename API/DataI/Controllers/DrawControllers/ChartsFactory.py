from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.InfChart import InfChart
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
            return BoundaryLineChart(table, width, height, xColomn, quality, 'testerrr')

        if chartType == enums.ChartTypes.PointChart.value:
            return PointChart(table, width, height, xColomn, quality, 'testerrr')

        if chartType == enums.ChartTypes.VerticalBarChart.value:
            return BarChart(table, width, height, xColomn, quality, 'testerrr')

        if chartType == enums.ChartTypes.InfChart.value:
            return InfChart(table, xColomn, width, height, 'testerrr')

        if chartType == enums.ChartTypes.MultiplePieChart.value:
            return MultiplePieChart(table, xColomn, width, height, 'testerrr')

        if chartType == enums.ChartTypes.PyramidalChart.value:
            return PyramidalChart(table, xColomn, width, height, 'testerrr')

        if chartType == enums.ChartTypes.SmartPieChart.value:
            return SmartPieChart(table, xColomn, width, height, 'testerrr')
