from typing import List

from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnModel


class RowUtils():
    @classmethod
    def addTwoCellsLists(cls, firstList: List[CellModel], secondList: List[CellModel]) -> List[CellModel]:
        resultList = list()
        for cell1, cell2 in zip(firstList, secondList):

            if (cell1.type == enums.CellType.numeric.value) and (cell2.type == enums.CellType.numeric.value):
                resultValue = cell1 + cell2
            else:
                resultValue = cell1
            resultList.append(resultValue)
        return resultList

    @classmethod
    def getRowFromTable(cls, columns: List[ColumnModel], rowIndex: int) -> List[CellModel]:
        row = list()
        for column in columns:
            row.append(column.cells[rowIndex])
        return row

    @classmethod
    def updateRowInTable(cls, columns: List[ColumnModel], rowIndex: int, row: List[CellModel]):
        for column, i in zip(columns, range(len(columns))):
            column.cells[rowIndex].value = row[i].value
            column.cells[rowIndex].type = row[i].type

    @classmethod
    def removeRowFromTable(cls, columns: List[ColumnModel], rowIndex: int):
        for column in columns:
            column.cells.pop(rowIndex)