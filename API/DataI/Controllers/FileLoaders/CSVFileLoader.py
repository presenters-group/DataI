import pandas
import ntpath

from typing import List

from DataI.Controllers.FileLoaders.FileLoader import FileLoader
from DataI.Models.TableModel import TableModel


class CSVFileLoader(FileLoader):
    def loadFile(self, id) -> TableModel:
        csvFile = pandas.read_csv(self.filePath)
        FileLoader._fillNaNs(csvFile)
        csvDict = csvFile.to_dict()
        randomColors = FileLoader._generateRandomColorsList(len(csvDict.keys()))
        return FileLoader._generateTableFromDict(csvDict, ntpath.basename(self.filePath), id, randomColors)







