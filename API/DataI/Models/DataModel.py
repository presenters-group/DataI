from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.DashboardModel import DashboardModel


class CustomChart(ObjectDeserializer):
    def __init__(self, svg: str, chartName: str):
        self.svg = svg
        self.chartName = chartName


class DataModel(ObjectDeserializer):
    def __init__(self, dataSources: List[TableModel], visualizations: List[VisualizationModel],
                 dashboards: List[DashboardModel], filters: List[FilterModel], customCharts: List[CustomChart]):
        self.dataSources = dataSources
        self.visualizations = visualizations
        self.dashboards = dashboards
        self.filters = filters
        self.customCharts = customCharts

    def __str__(self):
        return 'data-sources:\n{}\nvisualizations:\n{}\ndashboards:\n{}\nfilters:\n{}\ncustom-charts:\n{}\n'\
            .format(len(self.dataSources), len(self.visualizations), len(self.dashboards),
                    len(self.filters), len(self.customCharts))

    @classmethod
    def from_json(cls, data):
        dataSourcesBuffer = data['dataSources']
        dataSources = list()
        for dataSource in dataSourcesBuffer:
            dataSources.append(TableModel.from_json(dataSource))

        visualizationsBuffer = data['visualizations']
        visualizations = list()
        for visualization in visualizationsBuffer:
            visualizations.append(VisualizationModel.from_json(visualization))


        dashboardsBuffer = data['dashboards']
        dashboards = list()
        for dashboard in dashboardsBuffer:
            dashboards.append(DashboardModel.from_json(dashboard))


        filtersBuffer = data['filters']
        filters = list()
        for filter in filtersBuffer:
            filters.append(FilterModel.from_json(filter))


        customChartsBuffer = data['customCharts']
        customCharts = list()
        for customChart in customChartsBuffer:
            customCharts.append(CustomChart.from_json(customChart))

        return cls(dataSources, visualizations, dashboards, filters, customCharts)






























