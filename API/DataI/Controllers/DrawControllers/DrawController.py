from copy import deepcopy
from typing import Dict, List

from numpy import double

from DataI.Controllers.DataControllers.DashboardsController import DashboardsController
from DataI.Controllers.DataControllers.DataSourcesController import DataSourcesController
from DataI.Controllers.DataControllers.VisualizationsController import VisualizationsController
from DataI.Controllers.DrawControllers.ChartsFactory import ChartsFactory
from DataI.Controllers.Filters.FiltersController import FiltersController
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel
from DataI.Controllers.DataControllers import DataController
from DataI.Models.VisualizationModel import VisualizationModel


class DrawController():
    @classmethod
    def generateVisualizerTable(cls, table: TableModel, visio: VisualizationModel) -> TableModel:
        columns = list()

        for columnId in visio.usedColumns:
            if columnId != visio.xColumn:
                columnIndex = DataController.getElementIndexById(table.columns, columnId)
                columns.append(table.columns[columnIndex])

        returnTable = TableModel(columns,
                                 table.name,
                                 table.id,
                                 table.properties,
                                 table.aggregator,
                                 table.filters,
                                 table.isDeleted)

        # setting used colors in table:
        # 1- rows:
        returnTable.rowsColors = table.rowsColors
        # 2- columns:
        columnsColors = list()
        for columnId in visio.usedColumns:
            if columnId != visio.xColumn:
                columnIndex = DataController.getElementIndexById(table.columns, columnId)
                columnsColors.append(table.columnsColors[columnIndex])
        returnTable.columnsColors = columnsColors

        return returnTable

    @classmethod
    def getChart(cls, data: DataModel, visioId: int, width: double, height: double,
                 tableFilter, dashboardId: int) -> Dict:
        visioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        visualizer = data.visualizations[visioIndex]

        # implement visualization filters.
        drawTable = tableFilter(data, dashboardId, visioId)

        drawTable = DataSourcesController.\
            sugreCoatAggregatedChartTable(data, drawTable, VisualizationsController.getFilteredTable, visualizer.id)


        xColumn = drawTable.columns[DataController.getElementIndexById(drawTable.columns, visualizer.xColumn)]

        drawTable = cls.generateVisualizerTable(drawTable, visualizer)

        drawer = ChartsFactory.generateCharts(visualizer.chart,
                                              drawTable, width, height, xColumn, double(visualizer.quality), visualizer.animation)

        chartDict = dict()
        chartDict['visualizerId'] = visioId
        chartDict['svg'] = drawer.SVG
        chartDict['metaData'] = drawer.metaData

        return chartDict

    @classmethod
    def getChartPNG(cls, data: DataModel, visioId: int, width: double, height: double,
                 tableFilter, dashboardId: int) -> str:
        visioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        visualizer = data.visualizations[visioIndex]

        # implement visualization filters.
        drawTable = tableFilter(data, dashboardId, visioId)

        drawTable = DataSourcesController. \
            sugreCoatAggregatedChartTable(data, drawTable, VisualizationsController.getFilteredTable, visualizer.id)

        xColumn = drawTable.columns[DataController.getElementIndexById(drawTable.columns, visualizer.xColumn)]

        drawTable = cls.generateVisualizerTable(drawTable, visualizer)

        drawer = ChartsFactory.generateCharts(visualizer.chart, drawTable,
                                              width, height, xColumn, double(visualizer.quality), visualizer.animation)

        return drawer.saveAsPNG()

    @classmethod
    def getChartSVG(cls, data: DataModel, visioId: int, width: double, height: double,
                 tableFilter, dashboardId: int) -> str:
        visioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        visualizer = data.visualizations[visioIndex]

        # implement visualization filters.
        drawTable = tableFilter(data, dashboardId, visioId)

        drawTable = DataSourcesController. \
            sugreCoatAggregatedChartTable(data, drawTable, VisualizationsController.getFilteredTable, visualizer.id)

        xColumn = drawTable.columns[DataController.getElementIndexById(drawTable.columns, visualizer.xColumn)]

        drawTable = cls.generateVisualizerTable(drawTable, visualizer)

        drawer = ChartsFactory.generateCharts(visualizer.chart,
                                              drawTable, width, height, xColumn, double(visualizer.quality), visualizer.animation)

        return drawer.saveAsSVG()


    @classmethod
    def getDashboardVisioChart(cls, data: DataModel, dashboardId: int, visioId: int) -> Dict:
        dashboardIndex = DataController.getElementIndexById(data.dashboards, dashboardId)
        dashboard = data.dashboards[dashboardIndex]
        inVisioIndex = cls.__getVisioIndexFromDashboard(dashboard, visioId)
        inVisio = dashboard.visualizers[inVisioIndex]

        return cls.getChart(data, inVisio.visualizationId,
                            inVisio.measurements['width'],
                            inVisio.measurements['height'],
                            DashboardsController.getFilteredChartTable, dashboardId)


    @classmethod
    def getAllDashboardCharts(cls, data: DataModel, dashboardId: int) -> List[Dict]:
        charts = list()
        targetDashboardIndex = DataController.getElementIndexById(data.dashboards, dashboardId)
        dashboard = data.dashboards[targetDashboardIndex]
        for inVisioModel in dashboard.visualizers:
            charts.append(cls.getDashboardVisioChart(data, dashboardId, inVisioModel.visualizationId))
        return charts

    @classmethod
    def __getVisioIndexFromDashboard(cls, dashboard: DashboardModel, visioId: int):
        indexCounter = 0
        for inVisioModel in dashboard.visualizers:
            if inVisioModel.visualizationId == visioId:
                return indexCounter
            indexCounter += 1
        return -1



























