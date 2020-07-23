from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicDataModelInfo


class VisualizationModel(ObjectDeserializer, BasicDataModelInfo):
    def __init__(self, data: int, usedColumns: List[int], xColumn: int, name: str, id: int,
                 chart: str, filters: List, quality: float, animation: bool, isDeleted: bool):
        super(VisualizationModel, self).__init__(name, id, filters, isDeleted)
        self.data = data
        self.usedColumns = usedColumns
        self.xColumn = xColumn
        self.chart = chart
        self.animation = animation
        self.quality = quality

    def __str__(self):
        return 'name: {}, ID: {}\ndata-source:\n{}' \
               '\nfilters:\n{}\nanimation: {}\nquality: {}\nisDeleted: {}\n'.\
            format(self.name, self.id, self.data, self.filters, self.animation, self.quality, self.isDeleted)








