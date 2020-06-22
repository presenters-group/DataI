from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo


class Measurements(ObjectDeserializer):
    def __init__(self, w: float, h: float, x: float, y: float):
        self.width = w
        self.height = h
        self.x = x
        self.y = y

    def __str__(self):
        return 'width: {}, height: {}, x: {}, y: {}'.format(self.width, self.height, self.x, self.y)


class InDashboardFilterModel(ObjectDeserializer):
    def __init__(self, filterIndex: int, measurements: Measurements):
        self.filterIndex = filterIndex
        self.measurements = measurements

    def __str__(self):
        return 'filter index: {}, measurements:\n{}\n'.format(self.filterIndex, self.measurements)


class InDashboardVisioModel(ObjectDeserializer):
    def __init__(self, visualizationIndex: int, displayedFilters: List[InDashboardFilterModel],
                 measurements: Measurements):
        self.visualizationIndex = visualizationIndex
        self.measurements = measurements
        self.displayedFilters = displayedFilters

    def __str__(self):
        return 'visualization index: {}\nmeasurements:\n{}\ndisplayed filters:\n{}\n' \
            .format(self.visualizationIndex, self.measurements, self.displayedFilters)


class DashboardModel(BasicInfo):
    def __init__(self, visualizers: List[InDashboardVisioModel], name: str, id: int):
        super(DashboardModel, self).__init__(name, id)
        self.visualizers = visualizers

    def __str__(self):
        return 'name: {}, ID: {}\nvisualizers:\n{}'.format(self.name, self.id, self.visualizers)

    @classmethod
    def from_json(cls, data):
        buffer = data['visualizers']
        visualizers = list()
        for element in buffer:
            visualizers.append(InDashboardVisioModel.from_json(element))
        name = data['name']
        id = data['id']
        return cls(visualizers, name, id)
