import pandas

from typing import List
from DataI.Controllers.FileLoaders.FileLoader import FileLoader
from DataI.Models.TableModel import TableModel


class ExcelFileLoader(FileLoader):
    def loadFile(self, id) -> List[TableModel]:
        tables = list()
        # to extract sheets names
        xlf = pandas.ExcelFile(self.filePath)
        sheetNames = xlf.sheet_names

        tableIdCounter = id
        for sheetName in sheetNames:
            xlLoader = pandas.read_excel(self.filePath, sheetName)
            FileLoader._fillNaNs(xlLoader)
            xlDict = xlLoader.to_dict()
            # generate random colors list with the length of the columns number.
            randomColumnsColors = FileLoader._generateRandomColorsList(len(xlDict.keys()))
            # generate random colors list with the length of the rows number.
            xlDictValues = xlDict.values()
            xlDictIterator = iter(xlDictValues)
            firstVaule = next(xlDictIterator)
            randomRowsColors = FileLoader._generateRandomColorsList(len(firstVaule))
            tables.append(FileLoader._generateTableFromDict(xlDict, sheetName, tableIdCounter, randomColumnsColors, randomRowsColors))
            tableIdCounter += 1
        return tables


