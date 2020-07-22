import os
import re
import zipfile
import io
import shutil
from os.path import basename

from typing import List
from DataI.Controllers.FileSaver.FileSaver import FileSaver
from DataI.Models.TableModel import TableModel


class CSVFileSaver(FileSaver):
    def saveFile(self, tables: List[TableModel]):
        filesDirs = list()
        for table, i in zip(tables, range(len(tables))):
            dataFrame = self.tableToDataFrameConverter(table)
            if i == 0:
                dataFrame.to_csv(self.fullFilePath, index=False)
                filesDirs.append(self.fullFilePath)
            else:
                extentionIndex = str(self.fullFilePath).find('.csv', re.IGNORECASE)
                path = self.fullFilePath[:extentionIndex] + str(i) + self.fullFilePath[extentionIndex:]
                dataFrame.to_csv(path, index=False)
                filesDirs.append(path)

        currentPath = os.path.dirname(__file__)
        csvFilePath = currentPath[:len(currentPath) - 27] + 'media/download/csvFile/'
        fileName = 'csvFiles.zip'

        ziph = zipfile.ZipFile(csvFilePath + fileName, 'w')

        for file in filesDirs:
            ziph.write(file)

        ziph.close()

    def saveSingleFile(self, table: TableModel):
        dataFrame = self.tableToDataFrameConverter(table)
        dataFrame.to_csv(self.fullFilePath, index=False)








