import re
from copy import deepcopy
from typing import List, Set

from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class Equation():
    @classmethod
    def implementEquation(cls, table: TableModel, equation: str, newName: str):
        columns = cls.extractColumnsFromEquation(table, equation)
        distinctNames = cls.extractDistinctNamesFromEquation(equation)

        moddedEquation = deepcopy(equation)

        for distinctName, index in zip(distinctNames, range(len(distinctNames))):
            moddedEquation = moddedEquation.replace(distinctName, cls.columnNameBuilder(index, 'columns'))

        print(moddedEquation)

        resultColumn = eval(moddedEquation)

        resultColumn.name = newName

        return resultColumn


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


def getColumnByName(table: TableModel, name: str) -> ColumnModel:
    for column in table.columns:
        if column.name == name:
            return column