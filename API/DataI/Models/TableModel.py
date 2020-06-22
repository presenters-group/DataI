from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo
from DataI.Models.ColumnModel import ColumnModel


class PropertiesModel(ObjectDeserializer):
    def __init__(self, sourceFileType: str, zoomValue: int):
        self.sourceFileType = sourceFileType
        self.zoomValue = zoomValue

    def __str__(self):
        return 'source file type: {}, zoom value: {}, x column: {}'.format(self.sourceFileType, self.zoomValue, self.xColumn)


class AggregationModel():
    def __init__(self, aggregatedTable: List[ColumnModel], aggregationColumn: int, isActive: bool):
        self.aggregatedTable = aggregatedTable
        self.aggregationColumn = aggregationColumn
        self.isActive = isActive

    def __str__(self):
        return 'aggregatedTable:\n{}, aggregationColumn: {}, is active: {}'\
            .format(self.aggregatedTable, self.aggregationColumn, self.isActive)

    @classmethod
    def from_json(cls, data):
        buffer = data['aggregatedTable']
        aggregatedTable = list()
        for element in buffer:
            aggregatedTable.append(ColumnModel.from_json(element))
        aggregationColumn = data['aggregationColumn']
        isActive = data['isActive']
        return cls(aggregatedTable, aggregationColumn, isActive)


class TableModel(BasicInfo):
    def __init__(self, columns: List[ColumnModel], name: str, id: int, properties: PropertiesModel,
                 aggregator: AggregationModel, isDeleted: bool):
        super().__init__(name, id)
        self.columns = columns

        bufferColumnsList = list()
        for col in columns:
            bufferColumnsList.append(True)
        self.columnsVisibility = bufferColumnsList

        buffeRowList = list()
        for i in range(self.__getLongestColumnLength(columns)):
            buffeRowList.append(True)

        self.rowsVisibility = buffeRowList

        self.properties = properties
        self.aggregator = aggregator
        self.isDeleted = isDeleted

    @classmethod
    def CreateWithVisibilityParams(self, columns: List[ColumnModel], name: str, id: int, properties: PropertiesModel,
                                   aggregator: AggregationModel, columnsVisibility, rowsVisibility, isDeleted: bool):
        self.columns = columns

        bufferColumnsList = list()
        for col in columns:
            bufferColumnsList.append(True)
        self.columnsVisibility = bufferColumnsList

        buffeRowList = list()
        for i in range(self.__getLongestColumnLength(columns)):
            buffeRowList.append(True)

        self.rowsVisibility = buffeRowList

        self.name = name
        self.id = id
        self.properties = properties
        self.aggregator = aggregator
        self.columnsVisibility = columnsVisibility
        self.rowsVisibility = rowsVisibility
        self.isDeleted = isDeleted
        return self

    @classmethod
    def __getLongestColumnLength(self, columns: List[ColumnModel]) -> int:
        max = 0
        for column in columns:
            if column.cells.__len__() > max:
                max = column.cells.__len__()
        return max


    def __str__(self):
        return 'name: {}, ID: {}\ncolumns:\n{}\nproperties: {}, aggregator:\n{}\nisDeleted: {}\n'\
            .format(self.name, self.id, self.columns, self.properties, self.aggregator, self.isDeleted)

    @classmethod
    def from_json(cls, data):
        buffer = data['columns']
        columns = list()
        for element in buffer:
            columns.append(ColumnModel.from_json(element))
        columnsVisibility = data['columnsVisibility']
        rowsVisibility = data['rowsVisibility']
        name = data['name']
        id = data['id']
        properties = PropertiesModel.from_json(data['properties'])
        aggregator = AggregationModel.from_json(data['aggregator'])
        isDeleted = data['isDeleted']
        print('here')
        return cls.CreateWithVisibilityParams(columns, name, id, properties, aggregator,
                                              columnsVisibility, rowsVisibility, isDeleted)















