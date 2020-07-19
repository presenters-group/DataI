from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel
from DataI.Models.FilterModel import FilterModel
from DataI.Models.DashboardModel import DashboardModel


class DataModel(ObjectDeserializer):
    def __init__(self, dataSources: List[TableModel], visualizations: List[VisualizationModel],
                 dashboards: List[DashboardModel], filters: List[FilterModel]):
        self.dataSources = dataSources
        self.visualizations = visualizations
        self.dashboards = dashboards
        self.filters = filters

    def __str__(self):
        return 'dataSourceTableWithoutXcolumn sources:\n{}\nvisualizations:\n{}\ndashboards:\n{}\n'\
            .format(self.dataSources, self.visualizations, self.dashboards, self.filters)

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

        return cls(dataSources, visualizations, dashboards, filters)






























