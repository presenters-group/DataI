import pandas

from typing import List
from DataI.Controllers.FileSaver.FileSaver import FileSaver
from DataI.Models.TableModel import TableModel


class ExcelFileSaver(FileSaver):
    def saveFile(self, tables: List[TableModel]):
        writer = pandas.ExcelWriter(self.fullFilePath, engine='xlsxwriter')

        for table in tables:
            dataFrame = self.tableToDataFrameConverter(table)
            dataFrame.to_excel(writer, sheet_name=table.name, index=False)

        writer.save()



























