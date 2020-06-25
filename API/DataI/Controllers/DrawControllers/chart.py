from numpy import double

from DataI.Models.TableModel import TableModel


class Chart:
  def __init__(self, dataSource: TableModel, width: double, height: double):
    self.data = dataSource
    self.widthView = width
    self.heightView = height
