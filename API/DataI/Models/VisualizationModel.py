from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicDataModelInfo


class VisualizationModel(ObjectDeserializer, BasicDataModelInfo):
    def __init__(self, data: int, usedColumns: List[int], xColumn: int, name: str, id: int,
                 chart: str, filters: List, animation: bool, isDeleted: bool):
        super(VisualizationModel, self).__init__(name, id, filters, isDeleted)
        self.data = data
        self.usedColumns = usedColumns
        self.xColumn = xColumn
        self.chart = chart
        self.animation = animation

    def __str__(self):
        return 'name: {}, ID: {}\ndataSourceTableWithoutXcolumn:\n{}\nfilters:\n{}\nanimation: {}\nisDeleted: {}\n'.\
            format(self.name, self.id, self.data, self.filters, self.animation, self.isDeleted)








