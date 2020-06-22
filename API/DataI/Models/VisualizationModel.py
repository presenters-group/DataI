from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo


class VisualizationModel(ObjectDeserializer, BasicInfo):
    def __init__(self, data: int, usedColumns: List[int], xColumn: int, name: str, id: int, chart: str, filters: List[int], isDeleted: bool):
        super(VisualizationModel, self).__init__(name, id)
        self.data = data
        self.usedColumns = usedColumns
        self.xColumn = xColumn
        self.chart = chart
        self.filters = filters
        self.isDeleted = isDeleted

    def __str__(self):
        return 'name: {}, ID: {}\ndata:\n{}\nfilters:\n{}\nisDeleted: {}\n'.format(self.name, self.id, self.data, self.filters, self.isDeleted)








