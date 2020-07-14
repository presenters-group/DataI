import ntpath

import pandas

from DataI.Controllers.FileLoaders.FileLoader import FileLoader
from DataI.Models.TableModel import TableModel


class CSVFileLoader(FileLoader):
    def loadFile(self, id) -> TableModel:
        csvFile = pandas.read_csv(self.filePath)
        FileLoader._fillNaNs(csvFile)
        csvDict = csvFile.to_dict()
        # generate random colors list with the length of the columns number.
        randomColumnsColors = FileLoader._generateRandomColorsList(len(csvDict.keys()))
        # generate random colors list with the length of the rows number.
        csvDictValues = csvDict.values()
        csvDictIterator = iter(csvDictValues)
        firstVaule = next(csvDictIterator)
        randomRowsColors = FileLoader._generateRandomColorsList(len(firstVaule))
        return FileLoader._generateTableFromDict(csvDict, ntpath.basename(self.filePath), id, randomColumnsColors, randomRowsColors)
