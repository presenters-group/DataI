from numpy import double, long
from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel
import drawSvg as draw

class Chart:
  def __init__(self,dataSource:TableModel,width:double,height:double):
    self.data = dataSource
    self.widthView = width
    self.heightView = height

