import sys
import traceback
from typing import List

from dateutil.parser import parse

from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo
from DataI import enums
from DataI.Models.Exceptions import DifferentTypesException, TwoStringsException


class CellModel(ObjectDeserializer):

    def __init__(self, value, type: str):
        self.value = value
        self.type = type

    def __str__(self):
        return 'value: {}, type: {}'.format(self.value, self.type)

    def __add__(self, other):
        # handling a number operand.
        if type(other) != CellModel:
            if self.type == enums.CellType.string.value and type(other) == str:
                raise TwoStringsException('Can not add two strings as a mathematical operation.')

            if self.type == enums.CellType.numeric.value and type(other) == str:
                raise DifferentTypesException('Can not add type: {} to type: {}.'.format(self.type, type(other)))

            if self.type == enums.CellType.string.value  and type(other) != str:
                raise DifferentTypesException('Can not add type: {} to type: {}.'.format(self.type, type(other)))

            return CellModel(self.value + other, self.type)

        if self.type != other.type:
            raise DifferentTypesException('Can not add type: {} to type: {}.'.format(self.type, other.type))

        if (self.type and other.type) is enums.CellType.string.value:
            raise TwoStringsException('Can not add two strings as a mathematical operation.')

        return CellModel(self.value + other.value, self.type)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        # handling a number operand.
        if type(other) != CellModel:
            if self.type == enums.CellType.string.value and type(other) == str:
                raise TwoStringsException('Can not subtract two strings as a mathematical operation.')

            if self.type == enums.CellType.numeric.value and type(other) == str:
                raise DifferentTypesException('Can not subtract type: {} to type: {}.'.format(self.type, type(other)))

            if self.type == enums.CellType.string.value and type(other) != str:
                raise DifferentTypesException('Can not subtract type: {} to type: {}.'.format(self.type, type(other)))

            return CellModel(self.value - other, self.type)

        if self.type != other.type:
            raise DifferentTypesException('Can not subtract type: {} to type: {}.'.format(self.type, other.type))

        if (self.type and other.type) is enums.CellType.string.value:
            raise TwoStringsException('Can not subtract two strings as a mathematical operation.')

        return CellModel(self.value - other.value, self.type)

    def __rsub__(self, other):
        # handling a number operand.
        if type(other) != CellModel:
            if self.type == enums.CellType.string.value and type(other) == str:
                raise TwoStringsException('Can not subtract two strings as a mathematical operation.')

            if self.type == enums.CellType.numeric.value and type(other) == str:
                raise DifferentTypesException('Can not subtract type: {} to type: {}.'.format(self.type, type(other)))

            if self.type == enums.CellType.string.value and type(other) != str:
                raise DifferentTypesException('Can not subtract type: {} to type: {}.'.format(self.type, type(other)))

            return CellModel(other - self.value, self.type)

        if self.type != other.type:
            raise DifferentTypesException('Can not subtract type: {} to type: {}.'.format(self.type, other.type))

        if (self.type and other.type) is enums.CellType.string.value:
            raise TwoStringsException('Can not subtract two strings as a mathematical operation.')

        return CellModel(other.value - self.value, self.type)

    def __mul__(self, other):
        # handling a number operand.
        if type(other) != CellModel:
            if self.type == enums.CellType.string.value and type(other) == str:
                raise TwoStringsException('Can not multiply two strings as a mathematical operation.')

            if self.type == enums.CellType.numeric.value and type(other) == str:
                raise DifferentTypesException('Can not multiply type: {} to type: {}.'.format(self.type, type(other)))

            if self.type == enums.CellType.string.value and type(other) != str:
                raise DifferentTypesException('Can not multiply type: {} to type: {}.'.format(self.type, type(other)))

            return CellModel(self.value * other, self.type)

        if self.type != other.type:
            raise DifferentTypesException('Can not multiply type: {} to type: {}.'.format(self.type, other.type))

        if (self.type and other.type) is enums.CellType.string.value:
            raise TwoStringsException('Can not multiply two strings as a mathematical operation.')

        return CellModel(self.value * other.value, self.type)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # handling a number operand.
        if type(other) != CellModel:
            if self.type == enums.CellType.string.value and type(other) == str:
                raise TwoStringsException('Can not divide two strings as a mathematical operation.')

            if self.type == enums.CellType.numeric.value and type(other) == str:
                raise DifferentTypesException('Can not divide type: {} to type: {}.'.format(self.type, type(other)))

            if self.type == enums.CellType.string.value and type(other) != str:
                raise DifferentTypesException('Can not divide type: {} to type: {}.'.format(self.type, type(other)))

            try:
                returnValue = self.value / other
            except ZeroDivisionError:
                raise ZeroDivisionError('Can not divide by zero')

            return CellModel(returnValue, self.type)

        if self.type != other.type:
            raise DifferentTypesException('Can not divide type: {} to type: {}.'.format(self.type, other.type))

        if (self.type and other.type) is enums.CellType.string.value:
            raise TwoStringsException('Can not divide two strings as a mathematical operation.')

        try:
            returnValue = self.value / other.value
        except:
            raise ZeroDivisionError('Can not divide by zero')

        return CellModel(returnValue, self.type)

    def __rtruediv__(self, other):
        # handling a number operand.
        if type(other) != CellModel:
            if self.type == enums.CellType.string.value and type(other) == str:
                raise TwoStringsException('Can not divide two strings as a mathematical operation.')

            if self.type == enums.CellType.numeric.value and type(other) == str:
                raise DifferentTypesException('Can not divide type: {} to type: {}.'.format(self.type, type(other)))

            if self.type == enums.CellType.string.value and type(other) != str:
                raise DifferentTypesException('Can not divide type: {} to type: {}.'.format(self.type, type(other)))

            try:
                returnValue = other / self.value
            except ZeroDivisionError:
                raise ZeroDivisionError('Can not divide by zero')

            return CellModel(returnValue, self.type)

        if self.type != other.type:
            raise DifferentTypesException('Can not divide type: {} to type: {}.'.format(self.type, other.type))

        if (self.type and other.type) is enums.CellType.string.value:
            raise TwoStringsException('Can not divide two strings as a mathematical operation.')

        try:
            returnValue = other.value / self.value
        except:
            raise ZeroDivisionError('Can not divide by zero')

        return CellModel(returnValue, self.type)



class ColumnStyleModel(ObjectDeserializer):
    def __init__(self, color: str, lineWeight: float, pointWeight: float, font: str):
        self.color = color
        self.lineWeight = lineWeight
        self.pointWeight = pointWeight
        self.font = font

    def __str__(self):
        return 'color: {}, line weight: {}, point weight: {}, font: {}' \
            .format(self.color, self.lineWeight, self.pointWeight, self.font)


class ColumnModel(BasicInfo):
    def __init__(self, cells: List[CellModel], name: str, id: int, isDeleted: bool):
        super(ColumnModel, self).__init__(name, id, isDeleted)
        self.cells = cells
        self.columnType = self.__getColumnType(cells[1:])
        self.valueCategories = list()

        for cell in cells[1:]:
            if not self.__cellInList(cell, self.valueCategories):
                self.valueCategories.append(cell)

    def __str__(self):
        return 'name: {}, ID: {}\ncells: {}\n<<type: {}>>\ncategories: {}\nisDeleted: {}\n' \
            .format(self.name, self.id, self.cells, self.columnType, self.valueCategories, self.isDeleted)

    def __add__(self, other):
        cells = list()
        cells.append(CellModel(self.name, enums.CellType.string.value))

        if type(other) != ColumnModel:
            for cell in self.cells[1:]:
                try:
                    newCell = cell + other

                except DifferentTypesException:
                    raise DifferentTypesException('can not add a value that is of a different type to a column.')

                except TwoStringsException:
                    raise DifferentTypesException('can not add a string value to a string column.')

                cells.append(newCell)

            return ColumnModel(cells, self.name, self.id, self.isDeleted)

        for cell, i in zip(self.cells[1:], range(1, len(self.cells))):
            try:
                newCell = cell + other.cells[i]

            except DifferentTypesException:
                raise DifferentTypesException('can not add two columns that have cells with different types.')

            except TwoStringsException:
                raise DifferentTypesException('can not add two columns that have cells that are of type string.')

            cells.append(newCell)

        return ColumnModel(cells, self.name, self.id, self.isDeleted)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        cells = list()
        cells.append(CellModel(self.name, enums.CellType.string.value))

        if type(other) != ColumnModel:
            for cell in self.cells[1:]:
                try:
                    newCell = cell - other

                except DifferentTypesException:
                    raise DifferentTypesException('can not subtract a column that is of a different type from a value.')

                except TwoStringsException:
                    raise DifferentTypesException('can not subtract a string column from a string value.')

                cells.append(newCell)

            return ColumnModel(cells, self.name, self.id, self.isDeleted)

        for cell, i in zip(self.cells[1:], range(1, len(self.cells))):
            try:
                newCell = cell - other.cells[i]

            except DifferentTypesException:
                raise DifferentTypesException('can not subtract two columns that have cells with different types.')

            except TwoStringsException:
                raise DifferentTypesException('can not subtract two columns that have cells that are of type string.')

            cells.append(newCell)

        return ColumnModel(cells, self.name, self.id, self.isDeleted)

    def __rsub__(self, other):
        cells = list()
        cells.append(CellModel(self.name, enums.CellType.string.value))

        if type(other) != ColumnModel:
            for cell in self.cells[1:]:
                try:
                    newCell = other - cell

                except DifferentTypesException:
                    raise DifferentTypesException('can not subtract value that is of a different type from a column.')

                except TwoStringsException:
                    raise DifferentTypesException('can not subtract string value from a column.')

                cells.append(newCell)

            return ColumnModel(cells, self.name, self.id, self.isDeleted)

        for cell, i in zip(self.cells[1:], range(1, len(self.cells))):
            try:
                newCell = other.cells[i] - cell

            except DifferentTypesException:
                raise DifferentTypesException('can not subtract two columns that have cells with different types.')

            except TwoStringsException:
                raise DifferentTypesException('can not subtract two columns that have cells that are of type string.')

            cells.append(newCell)

        return ColumnModel(cells, self.name, self.id, self.isDeleted)

    def __mul__(self, other):
        cells = list()
        cells.append(CellModel(self.name, enums.CellType.string.value))

        if type(other) != ColumnModel:
            for cell in self.cells[1:]:
                try:
                    newCell = cell * other

                except DifferentTypesException:
                    raise DifferentTypesException('can not multiply a column that is of a different type by a value.')

                except TwoStringsException:
                    raise DifferentTypesException('can not multiply a string column with a string value.')

                cells.append(newCell)

            return ColumnModel(cells, self.name, self.id, self.isDeleted)

        for cell, i in zip(self.cells[1:], range(1, len(self.cells))):
            try:
                newCell = cell * other.cells[i]

            except DifferentTypesException:
                raise DifferentTypesException('can not multiply two columns that have cells with different types.')

            except TwoStringsException:
                raise DifferentTypesException('can not multiply two columns that have cells that are of type string.')

            cells.append(newCell)

        return ColumnModel(cells, self.name, self.id, self.isDeleted)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        cells = list()
        cells.append(CellModel(self.name, enums.CellType.string.value))

        if type(other) != ColumnModel:
            for cell in self.cells[1:]:
                try:
                    newCell = cell / other

                except DifferentTypesException:
                    raise DifferentTypesException('can not divide a column that is of a different type by a value.')

                except TwoStringsException:
                    raise DifferentTypesException('can not divide a string column by a string value.')

                except ZeroDivisionError:
                    raise ZeroDivisionError('can not divide column on a zero value.')

                cells.append(newCell)

            return ColumnModel(cells, self.name, self.id, self.isDeleted)

        for cell, i in zip(self.cells[1:], range(1, len(self.cells))):
            try:
                newCell = cell / other.cells[i]

            except DifferentTypesException:
                raise DifferentTypesException('can not divide two columns that have cells with different types.')

            except TwoStringsException:
                raise DifferentTypesException('can not divide two columns that have cells that are of type string.')

            except ZeroDivisionError:
                raise ZeroDivisionError('can not divide two columns that have cells produce zero division error.')

            cells.append(newCell)

        return ColumnModel(cells, self.name, self.id, self.isDeleted)

    def __rtruediv__(self, other):

        cells = list()
        cells.append(CellModel(self.name, enums.CellType.string.value))

        if type(other) != ColumnModel:
            for cell in self.cells[1:]:
                try:
                    newCell = other / cell

                except DifferentTypesException:
                    raise DifferentTypesException('can not divide column by a that is of a different type.')

                except TwoStringsException:
                    raise DifferentTypesException('can not divide column by a string value.')

                except ZeroDivisionError:
                    raise ZeroDivisionError('can not divide two columns that have cells produce zero division error.')

                cells.append(newCell)

            return ColumnModel(cells, self.name, self.id, self.isDeleted)

        for cell, i in zip(self.cells[1:], range(1, len(self.cells))):
            try:
                newCell = other.cells[i] / cell

            except DifferentTypesException:
                raise DifferentTypesException('can not divide two columns that have cells with different types.')

            except TwoStringsException:
                raise DifferentTypesException('can not divide two columns that have cells that are of type string.')

            except ZeroDivisionError:
                raise ZeroDivisionError('can not divide two columns that have cells produce zero division error.')

            cells.append(newCell)

        return ColumnModel(cells, self.name, self.id, self.isDeleted)

    def __cellInList(self, cell, list):
        for item in list:
            if item.value == cell.value:
                return True
        return False

    def __getColumnType(self, column: List[CellModel]) -> str:
        if self.__isDateColumn(column):
            return enums.ColumnDataType.DateTime.value


        for cell in column:
            isDigit = str(cell.value).replace('-', '').replace('.', '').isdigit()
            if not isDigit:
                return enums.ColumnDataType.Dimensions.value
        return enums.ColumnDataType.Measures.value

    def __isDateColumn(self, cells: List[CellModel]) -> bool:
        for cell in cells:
            try:
                buffer = parse(cell.value, fuzzy=False)
                cell.type = enums.CellType.DateTime.value
                # dateTimeObj = parse(cell.value, fuzzy=False)
                # if (dateTimeObj.day == 0 and dateTimeObj.month == 0) or\
                #         (dateTimeObj.day == 0 and dateTimeObj.year == 0) or\
                #         (dateTimeObj.month == 0 and dateTimeObj.year == 0):
                #     flag = False
                # else:
                #     flag = True
                flag = True
            except:
                flag = False

            if flag is False:
                return False

        return True


    @classmethod
    def from_json(cls, data):
        cells = list(map(CellModel.from_json, data["cells"]))
        name = data['name']
        id = data['id']
        isDeleted = data['isDeleted']
        return cls(cells, name, id, isDeleted)