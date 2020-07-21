from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicDataModelInfo
from DataI.Models.ColumnModel import ColumnModel



class PropertiesModel(ObjectDeserializer):
    def __init__(self, sourceFileType: str, zoomValue: int):
        self.sourceFileType = sourceFileType
        self.zoomValue = zoomValue

    def __str__(self):
        return 'source file type: {}, zoom value: {}'.format(self.sourceFileType, self.zoomValue)


class AggregationModel():
    def __init__(self, aggregatedTable: List[ColumnModel], aggregationColumn: int, type: str, isActive: bool):
        self.aggregatedTable = aggregatedTable
        self.aggregationColumn = aggregationColumn
        self.type = type
        self.isActive = isActive

    def __str__(self):
        return 'aggregatedTable:\n{}\naggregationColumn: {}, is active: {}'\
            .format(self.aggregatedTable, self.aggregationColumn, self.isActive)

    @classmethod
    def from_json(cls, data):
        buffer = data['aggregatedTable']
        aggregatedTable = list()
        for element in buffer:
            aggregatedTable.append(ColumnModel.from_json(element))
        aggregationColumn = data['aggregationColumn']
        type = data['type']
        isActive = data['isActive']
        return cls(aggregatedTable, aggregationColumn, type, isActive)


class TableModel(BasicDataModelInfo):
    def __init__(self, columns: List[ColumnModel], name: str, id: int, properties: PropertiesModel,
                 aggregator: AggregationModel, filters: List, isDeleted: bool):
        super().__init__(name, id, filters, isDeleted)
        self.columns = columns

        bufferColumnsList = list()
        for col in columns:
            bufferColumnsList.append(True)
        self.columnsVisibility = bufferColumnsList

        buffeRowList = list()
        for i in range(self.__getLongestColumnLength(columns) - 1):
            buffeRowList.append(True)

        self.rowsVisibility = buffeRowList

        self.columnsColors = List[str]
        self.rowsColors = List[str]

        self.properties = properties
        self.aggregator = aggregator
        self.isDeleted = isDeleted

    @classmethod
    def __getLongestColumnLength(self, columns: List[ColumnModel]) -> int:
        max = 0
        for column in columns:
            if column.cells.__len__() > max:
                max = column.cells.__len__()
        return max


    def __str__(self):
        return 'name: {}, ID: {}\ncolumns:\n{}\nproperties: {}\naggregator:\n{}\n'\
               'column colors:\n{}\nrows colors:\n{}\nfilters:\n{}\nisDeleted: {}\n'\
            .format(self.name, self.id, self.columns, self.properties, self.aggregator,
                    self.columnsColors, self.rowsColors, self.filters, self.isDeleted)

    @classmethod
    def from_json(cls, data):
        buffer = data['columns']
        columns = list()
        for element in buffer:
            columns.append(ColumnModel.from_json(element))

        columnsVisibility = data['columnsVisibility']
        rowsVisibility = data['rowsVisibility']

        columnsColors = data['columnsColors']
        rowsColors = data['rowsColors']

        name = data['name']
        id = data['id']
        properties = PropertiesModel.from_json(data['properties'])
        aggregator = AggregationModel.from_json(data['aggregator'])
        filters = data['filters']
        isDeleted = data['isDeleted']

        returnTable = cls(columns, name, id, properties, aggregator, filters, isDeleted)

        returnTable.columnsVisibility = columnsVisibility
        returnTable.rowsVisibility = rowsVisibility
        returnTable.columnsColors = columnsColors
        returnTable.rowsColors = rowsColors

        return returnTable

    def printTable(self):
        for i in range(len(self.columns[0].cells)):
            for j in range(len(self.columns)):
                print('{:20}'.format(self.columns[j].cells[i].value), end='')
            print()

    @classmethod
    def printColumns(cls, columns: List[ColumnModel]):
        for i in range(len(columns[0].cells)):
            for j in range(len(columns)):
                print('{:20}'.format(columns[j].cells[i].value), end='')
            print()
