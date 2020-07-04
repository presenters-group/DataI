import random
from typing import List, Dict

import pandas

from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel


class FileLoader():
    filePath = ''

    def __init__(self, filePath: str):
        self.filePath = filePath

    @classmethod
    def _generateTableFromDict(cls, columns: dict, name: str, id: int,
                               randomColumnsColors: List, randomRowsColors: List) -> TableModel:
        columnIdCounter = 0
        bufferColumnsList = []
        for columnName in columns.keys():
            bufferColumnsList.append(cls._generateColumnFromDict(columns[columnName], columnName, columnIdCounter))
            columnIdCounter += 1

        properties = PropertiesModel(enums.FileType.Excel.value, 50)
        aggregator = AggregationModel([], 0, False)
        table = TableModel(bufferColumnsList, name, id, properties, aggregator, False)
        table.rowsColors = randomRowsColors
        table.columnsColors = randomColumnsColors
        return table

    @classmethod
    def _generateColumnFromDict(cls, cells: Dict, name: str, id: int) -> ColumnModel:
        # create cells list
        columnCells = [CellModel(name, enums.CellType.string.value)]
        for cell in cells.values():
            # get cell type
            isDigit = str(cell).replace('.', '').isdigit() or str(cell).replace('-', '').isdigit()
            # cell = str(cell)
            if isDigit:
                type = enums.CellType.numeric.value
                cell = float(cell)
            else:
                type = enums.CellType.string.value
                cell = str(cell)
            columnCells.append(CellModel(cell, type))
        return ColumnModel(columnCells, name, id, False)

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
