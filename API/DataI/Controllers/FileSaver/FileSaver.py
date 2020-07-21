from typing import Dict, List
from pandas import DataFrame
from DataI.Models.TableModel import TableModel


class FileSaver():
    fullFilePath = str

    def __init__(self, fullFilePath):
        self.fullFilePath = fullFilePath

    @classmethod
    def tableToDataFrameConverter(cls, table: TableModel) -> DataFrame:
        return DataFrame(cls.__getTableAsListOfRows(table), columns=cls.__getColumnsNames(table))

    @classmethod
    def __getTableAsListOfRows(cls, table: TableModel) ->List[list]:
        rowsCount = len(table.columns[0].cells)
        tableList = list()
        for i in range(rowsCount):
            bufferRowList = list()
            for j in range(len(table.columns)):
                bufferRowList.append(table.columns[j].cells[i].value)
            tableList.append(bufferRowList)

        return tableList[1:]

    @classmethod
    def __getColumnsNames(cls, table: TableModel) -> List[str]:
        names = list()
        for column in table.columns:
            names.append(column.name)
        return names



