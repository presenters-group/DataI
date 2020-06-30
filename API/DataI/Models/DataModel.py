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
