from numpy import double, os
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel
import drawSvg as draw


class Chart:
    def __init__(self, dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel, animation: bool):
        self.animation = animation
        self.d = draw.Drawing(0,0)
        self.Index = 0
        self.metaData = list()
        self.dataSourceTableWithoutXcolumn = dataSourceTableWithoutXcolumn
        self.xColumn = xcolumon
        self.widthView = widthView
        self.heightView = heightView
    def saveAsSVG (self)->str:
      current = os.path.dirname(__file__)
      filePath = current[:len(current) - 33] + 'media/download/svg/'
      self.d.saveSvg(filePath+'Chart.svg')
      return filePath+'Chart.svg'
    def saveAsPNG (self)->str:
      current = os.path.dirname(__file__)
      filePath = current[:len(current) - 33] + 'media/download/svg/'
      self.d.saveSvg(filePath+'Chart.png')
      return filePath+'Chart.png'

