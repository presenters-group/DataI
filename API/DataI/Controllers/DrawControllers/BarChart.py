from numpy import double

from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel
import drawSvg as draw


class BarChart(PointChart):
  def __init__(self, dataSource: TableModel, width: double, height: double, Xcolomn: ColumnModel, quality: double):
    super().__init__(dataSource, width, height, Xcolomn, quality)
    self.widthOfSingleColumn = self.calculatWidthOfColumn()
    self.drawlayOut()
    self.drawColumns()
    self.drawLineLevels()
    self.drawXpoints(double(20))
    self.drawColmunsColorList(double(20))
    self.drawSideLable()
    self.SVG = self.d.asSvg()

  def calculatWidthOfColumn(self) -> double:
    count = len(self.Xcolumn.cells)
    return double((200 / count))

  def FindYofRightEdgeOFCoulumn(self, index: int) -> double:
    if (index == 0):
      width = self.widthOfSingleColumn * (index + 1)
    else:
      width = self.widthOfSingleColumn * (index + 1)
    return double(width)

  def FindYofLeftEdgeOFCoulumn(self, index: int) -> double:
    if (index != 0):
      width = self.widthOfSingleColumn * (index)
      return double(width)
    else:
      return double(self.widthOfSingleColumn * (index))

  def drawColumns(self):
    for column in self.data.columns:
      add = 350 - (self.widthOfSingleColumn * (len(self.data.columns) - 2))
      if (column != self.Xcolumn):
        for cell, i in zip(column.cells, range(0, len(self.Xcolumn.cells))):
          if (i != 0):
            p = draw.Path(stroke_width=2, stroke=column.style.color,
                          fill=column.style.color, fill_opacity=0.5, id=str(self.Index))
            name = str(column.name)
            self.listOfIndexing.append(name)
            self.Index += 1
            p.M(self.FindYofLeftEdgeOFCoulumn(column.id) + add, self.convertY(self.findZeroInSVG()))
            p.L(self.FindYofLeftEdgeOFCoulumn(column.id) + add, self.convertY(double(cell.value)))
            p.H(self.FindYofRightEdgeOFCoulumn(column.id) + add)
            p.V(self.convertY(self.findZeroInSVG()))
            self.d.append(p)
            add += 150
