from typing import Dict, List

from numpy import double

from DataI.Controllers.DataControllers.VisualizationsController import VisualizationsController
from DataI.Controllers.DrawControllers.ChartsFactory import ChartsFactory
from DataI.Models.DashboardModel import DashboardModel
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel
from DataI.Controllers.DataControllers import DataController


class DrawController():
    @classmethod
    def generateVisualizerTable(cls, data: DataModel, visioID: int) -> TableModel:
        columns = list()
        visioIndex = DataController.getElementIndexById(data.visualizations, visioID)
        tableIndex = data.visualizations[visioIndex].data

        for columnId in data.visualizations[visioIndex].usedColumns:
            columnIndex = DataController.getElementIndexById(data.dataSources[tableIndex].columns, columnId)
            columns.append(data.dataSources[tableIndex].columns[columnIndex])

        returnTable = TableModel(columns,
                                 data.dataSources[tableIndex].name,
                                 data.dataSources[tableIndex].id,
                                 data.dataSources[tableIndex].properties,
                                 data.dataSources[tableIndex].aggregator,
                                 data.dataSources[tableIndex].filters,
                                 data.dataSources[tableIndex].isDeleted)

        # setting used colors in table:
        # 1- rows:
        returnTable.rowsColors = data.dataSources[tableIndex].rowsColors
        # 2- columns:
        columnsColors = list()
        for columnId in data.visualizations[visioIndex].usedColumns:
            columnIndex = DataController.getElementIndexById(data.dataSources[tableIndex].columns, columnId)
            columnsColors.append(data.dataSources[tableIndex].columnsColors[columnIndex])
        returnTable.columnsColors = columnsColors


        return returnTable

    @classmethod
    def getChart(cls, data: DataModel, visioId: int, width: double, height: double) -> Dict:

        visioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        visualizer = data.visualizations[visioIndex]

        drawTable = cls.generateVisualizerTable(data, visioId)
        cls.__removeXColumnIfExists(drawTable, visualizer.xColumn)

        # implement visualization filters.
        drawTable = VisualizationsController.getFinalTable(data, visioId)

        xColumnIndex = DataController.getElementIndexById(data.dataSources, visualizer.xColumn)
        xColumn = drawTable.columns[xColumnIndex]

        # for column in drawTable.columns:
        #     for cell in column.cells:
        #         print(cell)
        #     print('_________________________')

        drawer = ChartsFactory.generateCharts(visualizer.chart, drawTable, width, height, xColumn, double(8.0))
        chartDict = dict()
        chartDict['visualizerId'] = visioId
        chartDict['svg'] = drawer.SVG
        chartDict['metaData'] = drawer.metaData

        return chartDict

    @classmethod
    def __removeXColumnIfExists(ctablels, drawTable: TableModel, xColumnId: int):
        for column in drawTable.columns:
            if column.id == xColumnId:
                drawTable.columns.pop(DataController.getElementIndexById(drawTable.columns, xColumnId))
                return


    @classmethod
    def getDashboardVisio(cls, data: DataModel, dashboardId: int, visioId: int) -> Dict:
        targetDashboardIndex = DataController.getElementIndexById(data.dashboards, dashboardId)
        dashboard = data.dashboards[targetDashboardIndex]
        targetInVisioIndex = cls.__getVisioIdFromDashboard(dashboard, visioId)
        inVisio = dashboard.visualizers[targetInVisioIndex]
        chart = cls.getChart(data, inVisio.visualizationId, inVisio.measurements.width, inVisio.measurements.height)
        return chart

    @classmethod
    def getAllDashboardCharts(cls, data: DataModel, dashboardId: int) -> List[Dict]:
        charts = list()
        targetDashboardIndex = DataController.getElementIndexById(data.dashboards, dashboardId)
        dashboard = data.dashboards[targetDashboardIndex]
        for inVisioModel in dashboard.visualizers:
            charts.append(cls.getDashboardVisio(data, dashboardId, inVisioModel.visualizationId))
        return charts


    @classmethod
    def __getVisioIdFromDashboard(cls, dashboard: DashboardModel, visioId: int):
        indexCounter = 0
        for inVisioModel in dashboard.visualizers:
            if inVisioModel.visualizationId == visioId:
                return indexCounter
            indexCounter += 1
        return -1



























