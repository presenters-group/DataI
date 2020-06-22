import re

import pandas

from typing import List
from DataI.Controllers.FileSaver.FileSaver import FileSaver
from DataI.Models.TableModel import TableModel

class CSVFileSaver(FileSaver):
    def saveFile(self, tables: List[TableModel]):
        for table, i in zip(tables, range(len(tables))):
            dataFrame = self.tableToDataFrameConverter(table)
            if i == 0:
                dataFrame.to_csv(self.fullFilePath, index=False)
            else:
                extentionIndex = str(self.fullFilePath).find('.csv', re.IGNORECASE)
                path = self.fullFilePath[:extentionIndex] + str(i) + self.fullFilePath[extentionIndex:]
                dataFrame.to_csv(path, index=False)

