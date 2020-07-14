from numpy import double
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class Chart:
    def __init__(self, dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel):
        self.Index = 0
        self.metaData = list()
        self.dataSourceTableWithoutXcolumn = dataSourceTableWithoutXcolumn
        self.xColumn = xcolumon
        self.widthView = widthView
        self.heightView = heightView
