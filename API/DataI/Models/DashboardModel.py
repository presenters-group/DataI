from typing import List

from numpy import double

from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo, BasicDataModelInfo


class Measurements(ObjectDeserializer):
    def __init__(self, w: double, h: double, x: double, y: double):
        self.width = w
        self.height = h
        self.x = x
        self.y = y

    def __str__(self):
        return 'width: {}, height: {}, x: {}, y: {}'.format(self.width, self.height, self.x, self.y)


class InDashboardFilterModel(ObjectDeserializer):
    def __init__(self, filterId: int, visioId: int, value, isActive: bool, measurements: Measurements):
        self.filterId = filterId
        self.visioId = visioId
        self.value = value
        self.isActive = isActive
        self.measurements = measurements

    def __str__(self):
        return 'filter index: {}, measurements:\n{}\n'.format(self.filterId, self.measurements)


class InDashboardVisioModel(ObjectDeserializer):
    def __init__(self, visualizationId: int, measurements: Measurements):
        self.visualizationId = visualizationId
        self.measurements = measurements

    def __str__(self):
        return 'visualization index: {}\nmeasurements:\n{}\n'.format(self.visualizationId, self.measurements)


class DashboardModel(BasicDataModelInfo):
    def __init__(self, visualizers: List[InDashboardVisioModel], name: str, id: int,
                 filters: List, isDeleted: bool):
        super(DashboardModel, self).__init__(name, id, filters, isDeleted)
        self.visualizers = visualizers


    def __str__(self):
        return 'name: {}, ID: {}\nvisualizers:\n{}\nfilters:\n{}\n'\
            .format(self.name, self.id, self.visualizers, self.filters)

    @classmethod
    def from_json(cls, data):
        buffer = data['visualizers']
        visualizers = list()
        for element in buffer:
            visualizers.append(InDashboardVisioModel.from_json(element))
        name = data['name']
        id = data['id']
        filters = data['filters']
        isDeleted = data['isDeleted']
        return cls(visualizers, name, id, filters, isDeleted)
