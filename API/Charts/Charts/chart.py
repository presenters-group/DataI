from numpy import double, long
from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel
import drawSvg as draw

class Chart:
  def __init__(self,dataSourceTableWithoutXcolumn:TableModel,widthView:double,heightView:double,xcolumon:ColumnModel):
    self.dataSourceTableWithoutXcolumn = dataSourceTableWithoutXcolumn
    self.xColumn = xcolumon
    self.widthView = widthView
    self.heightView = heightView


