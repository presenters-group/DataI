import json

from DataI.Controllers.FileLoaders.FileLoader import FileLoader
from DataI.Models.DataModel import DataModel


class DataIFileLoader(FileLoader):
    def loadFile(self) -> DataModel:
        file = open(self.filePath, 'r')
        jsonString = str(file.read())
        return DataModel.from_json(json.loads(jsonString))

