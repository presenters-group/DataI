from typing import List
from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo
from DataI import enums


class CellModel(ObjectDeserializer):
    def __init__(self, value, type: str):
        self.value = value
        self.type = type

    def __str__(self):
        return 'value: {}, type: {}'.format(self.value, self.type)

    def __add__(self, other):
        if self.type != other.type:
            print('Can not add type: {} to type: {}.'.format(self.type, other.type))
            return None
        if (self.type and other.type) is enums.CellType.string.value:
            print('Can not add two strings as a mathematical operation.')
            return None
        return CellModel(self.value + other.value, self.type)


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
    def __init__(self, cells: List[CellModel], name: str, id: int, isDeleted: bool):
        super(ColumnModel, self).__init__(name, id)
        self.cells = cells
        self.columnType = self.__getColumnType(cells[1:])
        self.valueCategories = list()
        self.isDeleted = isDeleted

        for cell in cells[1:]:
            if not self.__cellInList(cell, self.valueCategories):
                self.valueCategories.append(cell)

    def __str__(self):
        return 'name: {}, ID: {}\ncells: {}\n<<type: {}>>\ncategories: {}\nisDeleted: {}\n'\
            .format(self.name, self.id, self.cells, self.columnType, self.valueCategories, self.isDeleted)

    def __add__(self, other):
        cells = list()
        for cell, i in zip(self.cells, range(len(self.cells))):
            cells.append(CellModel(cell + other.cells[i], cell.type))
        return ColumnModel(cells, self.name, self.id, self.isDeleted)


    def __cellInList(self, cell, list):
        for item in list:
            if item.value == cell.value:
                return True
        return False

    def __getColumnType(self, column: List[CellModel]):
        for cell in column:
          isDigit = str(cell.value).replace('.', '').isdigit() or str(cell.value).replace('-', '').isdigit()
          if not isDigit:
                return enums.ColumnDataType.Dimensions.value

        return enums.ColumnDataType.Measures.value

    @classmethod
    def from_json(cls, data):
        cells = list(map(CellModel.from_json, data["cells"]))
        name = data['name']
        id = data['id']
        isDeleted = data['isDeleted']
        return cls(cells, name, id, isDeleted)
















