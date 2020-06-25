import random
import re

import pandas
from typing import List, Dict
from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel


class FileLoader():
    filePath = ''

    def __init__(self, filePath: str):
        self.filePath = filePath

    @classmethod
    def _generateTableFromDict(cls, columns: dict, name: str, id: int, randomColors: List) -> TableModel:
        columnIdCounter = 0
        bufferColumnsList = []
        for columnName in columns.keys():
            bufferColumnsList.append(cls._generateColumnFromDict(columns[columnName], columnName, columnIdCounter,
                                                                   randomColors[columnIdCounter]))
            columnIdCounter += 1

        properties = PropertiesModel(enums.FileType.Excel.value, 50)
        aggregator = AggregationModel([], 0, False)
        return TableModel(bufferColumnsList, name, id, properties, aggregator, False)

    @classmethod
    def _generateColumnFromDict(cls, cells: Dict, name: str, id: int, randomColumnColor: str) -> ColumnModel:
        # create cells list
        columnCells = [CellModel(name, enums.CellType.string.value)]
        for cell in cells.values():
            # get cell type
            cell = str(cell)
            if cell.isnumeric():
                type = enums.CellType.numeric.value
            else:
                type = enums.CellType.string.value
            columnCells.append(CellModel(cell, type))
        # create column style:
        style = ColumnStyleModel(randomColumnColor, 1.0, 1.0, 'Calibri')
        return ColumnModel(columnCells, name, id, style, False)

    @classmethod
    def _generateRandomColorsList(cls, listLength) -> List[str]:
        colorsList = []

        for i in range(listLength):
            random_color = random.randint(0, 16777215)
            hex_color = str(hex(random_color))
            hex_color = '#' + hex_color[2:]
            colorsList.append(hex_color)

        return colorsList

    @classmethod
    def _fillNaNs(cls, dataFrame: pandas.DataFrame):
        for (columnName, columnValue) in dataFrame.iteritems():
            dataFrame[columnName] = dataFrame[columnName].fillna(0)

