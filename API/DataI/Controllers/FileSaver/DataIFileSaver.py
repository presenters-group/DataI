import json

from DataI.Controllers.FileSaver.FileSaver import FileSaver
from DataI.JSONSerializer import ObjectEncoder
from DataI.Models.DataModel import DataModel


class DataIFileSaver(FileSaver):
    def saveFile(self, data: DataModel):
        writer = open(self.fullFilePath, 'wb')
        jsonString = json.dumps(data, indent=4, cls=ObjectEncoder, ensure_ascii=False)
        writer.write(bytes(jsonString))