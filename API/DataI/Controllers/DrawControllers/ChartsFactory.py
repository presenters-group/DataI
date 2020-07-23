import os

from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.BoundaryLineChart import BoundaryLineChart
from DataI.Controllers.DrawControllers.CustomChart import CustomChart
from DataI.Controllers.DrawControllers.FemaleAndMaleChart import FemaleAndMaleChart
from DataI.Controllers.DrawControllers.FemaleInfChart import FemaleInfChart
from DataI.Controllers.DrawControllers.HealthyFoodChart import HealthyFoodChart
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Controllers.DrawControllers.LineChart import LineChart
from DataI.Controllers.DrawControllers.MapChart import MapChart
from DataI.Controllers.DrawControllers.MapChartByLatitudeAndLongitude import MapChartByLatitudeAndLongitude
from DataI.Controllers.DrawControllers.MultiplePieChart import MultiplePieChart
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Controllers.DrawControllers.PyramidalChart import PyramidalChart
from DataI.Controllers.DrawControllers.SmatPieChart import SmartPieChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class ChartsFactory():

    @classmethod
    def generateCharts(cls, chartType: str, table: TableModel,
                       width: double, height: double, xColomn: ColumnModel, quality: double, animation: bool):

        if chartType == enums.ChartTypes.BoundaryLineChart.value:
            return BoundaryLineChart(table, width, height, xColomn, quality, animation, 'testerrr')

        if chartType == enums.ChartTypes.LineChart.value:
            return LineChart(table, width, height, xColomn, quality, animation, '')

        if chartType == enums.ChartTypes.PointChart.value:
            return PointChart(table, width, height, xColomn, quality, animation, 'testerrr')

        if chartType == enums.ChartTypes.VerticalBarChart.value:
            return BarChart(table, width, height, xColomn, quality, animation, 'testerrr')

        if chartType == enums.ChartTypes.InfChart.value:
            return InfChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.MultiplePieChart.value:
            return MultiplePieChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.PyramidalChart.value:
            return PyramidalChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.SmartPieChart.value:
            return SmartPieChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.FemaleAndMaleChart.value:
            return FemaleAndMaleChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.FemaleInfChart.value:
            return FemaleInfChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.HealthyFoodChart.value:
            return HealthyFoodChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.MapChart.value:
            return MapChart(table, xColomn, width, height, animation, 'testerrr')

        if chartType == enums.ChartTypes.MapChartByLatitudeAndLongitude.value:
            return MapChartByLatitudeAndLongitude(table, xColomn, width, height, animation, 'testerrr')

        else:
            current = os.path.dirname(__file__)
            current = current[:len(current) - 33] + 'media/uploads/svg/'
            filePath = current + chartType + '.svg'
            return CustomChart(table, xColomn, width, height, animation, filePath, filePath)









