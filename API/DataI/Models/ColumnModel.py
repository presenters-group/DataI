from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo
from DataI import enums


class CellModel(ObjectDeserializer):
    def __init__(self, value: object, type: str):
        self.value = value
        self.type = type

    def __str__(self):
        return 'value: {}, type: {}'.format(self.value, self.type)


class ColumnStyleModel(ObjectDeserializer):
    def __init__(self, color: str, lineWeight: float, pointWeight: float, font: str):
        self.color = color
        self.lineWeight = lineWeight
        self.pointWeight = pointWeight
        self.font = font

    def __str__(self):
        return 'color: {}, line weight: {}, point weight: {}, font: {}'\
            .format(self.color, self.lineWeight, self.pointWeight,self.font)


class ColumnModel(BasicInfo):
    def __init__(self, cells: List[CellModel], name: str, id: int, style: ColumnStyleModel, isDeleted: bool):
        super(ColumnModel, self).__init__(name, id)
        self.cells = cells
        self.style = style
        self.columnType = self.__getColumnType(cells[1:])
        self.valueCategories = list()
        self.isDeleted = isDeleted

        for cell in cells:
            if not self.__cellInList(cell, self.valueCategories):
                self.valueCategories.append(cell)

    def __str__(self):
        return 'name: {}, ID: {}\ncells: {}\n<<style: {}, type: {}>>\ncategories: {}\nisDeleted: {}\n'\
            .format(self.name, self.id, self.cells, self.style, self.columnType, self.valueCategories, self.isDeleted)

    def __cellInList(self, cell, list):
        for item in list:
            if item.value == cell.value:
                return True
        return False

    def __getColumnType(self, column: List[CellModel]):
        for cell in column:
            if not str(cell.value).isnumeric():
                return enums.ColumnDataType.Dimensions.value

        return enums.ColumnDataType.Measures.value

    @classmethod
    def from_json(cls, data):
        cells = list(map(CellModel.from_json, data["cells"]))
        name = data['name']
        id = data['id']
        style = ColumnStyleModel.from_json(data['style'])
        isDeleted = data['isDeleted']
        return cls(cells, name, id, style, isDeleted)
















