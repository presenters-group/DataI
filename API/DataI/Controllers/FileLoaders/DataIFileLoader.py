import json
import os
from typing import List

from DataI.Controllers.FileLoaders.FileLoader import FileLoader
from DataI.Models.DataModel import DataModel, CustomChart


class DataIFileLoader(FileLoader):
    def loadFile(self) -> DataModel:
        file = open(self.filePath, 'rb')
        jsonString = file.read()
        dataModel = DataModel.from_json(json.loads(jsonString))
        self.writeCustomChartsToUploads(dataModel.customCharts)
        return dataModel

    def writeCustomChartsToUploads(self, customCharts: List[CustomChart]):
        current = os.path.dirname(__file__)
        current = current[:len(current) - 29] + 'media/uploads/svg/'
        for customChart in customCharts:
            bufferPath = current + customChart.chartName + '.svg'
            svg = customChart.svg.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf-8')

            fileHandler = open(bufferPath, 'w')

            fileHandler.write(svg)


