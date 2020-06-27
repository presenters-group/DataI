from numpy import double

from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel
import drawSvg as draw


class BoundaryLineChart(PointChart):
  def __init__(self, dataSource: TableModel, width: double, height: double, Xcolomn: ColumnModel, quality: double):
    super().__init__(dataSource, width, height, Xcolomn, quality)
    self.drawLines()
    self.SVG = self.d.asSvg()

  def drawLines(self):
    for column in self.data.columns:
      add = 350
      p = draw.Path(stroke_width=2, stroke=column.style.color,
                    fill=column.style.color, fill_opacity=0.1, id=str(self.Index))
      name = str(column.name)
      self.listOfIndexing.append(name)
      self.Index += 1
      p.M(add, self.convertY(self.findZeroInSVG()))
      if (column != self.Xcolumn):
        for cell, i in zip(column.cells, range(0, len(self.Xcolumn.cells))):
          if (i != 0):
            p.L(add, self.convertY(double(cell.value)))
            add += 150
      p.V(self.convertY(self.findZeroInSVG()))
      self.d.append(p)
