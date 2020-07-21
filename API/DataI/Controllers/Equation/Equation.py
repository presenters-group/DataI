import re
from copy import deepcopy
from random import random
from typing import List, Set

from DataI import enums
from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Models.ColumnModel import ColumnModel, CellModel
from DataI.Models.TableModel import TableModel


class Equation():
    @classmethod
    def implementEquation(cls, table: TableModel, equation: str, newName: str):
        columns = cls.extractColumnsFromEquation(table, equation)
        distinctNames = cls.extractDistinctNamesFromEquation(equation)

        moddedEquation = deepcopy(equation)

        for distinctName, index in zip(distinctNames, range(len(distinctNames))):
            moddedEquation = moddedEquation.replace(distinctName, cls.columnNameBuilder(index, 'columns'))

        resultColumn = eval(moddedEquation)

        resultColumn.name = newName
        resultColumn.cells[0] = CellModel(newName, enums.CellType.string.value)
        resultColumn.id = DataController.getMaxIdInList(table.columns) + 1

        table.columnsVisibility.append(True)
        table.columnsColors.append(cls.__generateRandomColor())

        table.columns.append(resultColumn)

        return table

    @classmethod
    def extractColumnsFromEquation(cls, table: TableModel, equation: str) -> List[ColumnModel]:
        distinctNames = cls.extractDistinctNamesFromEquation(equation)

        # extract columns as objects.
        columns = list()
        for distinctName in distinctNames:
            bufferColumn = getColumnByName(table, distinctName)
            if bufferColumn is not None:
                columns.append(bufferColumn)

        return columns

    @classmethod
    def extractDistinctNamesFromEquation(cls, equation: str) -> Set:
        res = re.sub('\W+', ',', equation)
        names = res.split(',')

        # remove empty strings from the names list.
        for name, index in zip(names, range(len(names))):
            if name == '':
                names.pop(index)

        return set(names)

    @classmethod
    def columnNameBuilder(cls, index: int, listName: str) -> str:
        return listName + '[' + str(index) + ']'

    @classmethod
    def __generateRandomColor(cls) -> str:
        random_color = random.randint(0, 16777215)
        hex_color = str(hex(random_color))
        hex_color = '#' + hex_color[2:]
        return hex_color


def getColumnByName(table: TableModel, name: str) -> ColumnModel:
    for column in table.columns:
        if column.name == name:
            return column