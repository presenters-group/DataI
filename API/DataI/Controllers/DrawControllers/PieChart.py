from numpy import double, long, cos, sin

from Charts.Charts.chart import Chart
from DataI import enums
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel
import drawSvg as draw


class PieChart:
  def __init__(self, firstcColumon: ColumnModel, secondColumn: ColumnModel, width: double, height: double):
    self.widthView = width
    self.heightView = height
    self.firstColumn = firstcColumon
    self.secandColumn = secondColumn
    self.r = min(width, height)
    self.d = draw.Drawing(self.widthView, self.heightView)
    self.total = self.sumColumn(secondColumn)
    self.xCenter = self.yCenter = (self.r / 2)
    self.P = int(2 * 3.14 * self.r)
    self.drawCircle()
    self.SVG = self.d.asSvg()

  def drawlayOut(self):
    self.d.append(draw.Rectangle(0, 0, 1, 1, fill='#ffffff'))

  def sumColumn(self, column: ColumnModel) -> double:
    sum = 0.0
    for cell, i in zip(column.cells, range(0, len(column.cells))):
      if (i != 0):
        sum += cell.value
    return double(sum)

  def percentageOfValue(self, value: double) -> double:
    return double((value / self.total) * 100)

  def getLength(self, value: double) -> int:
    percent = self.percentageOfValue(value)
    return int((self.P / 100) * percent)

  def drawCircle(self):
    p = draw.Path(stroke_width=1, stroke='black', fill='gray', fill_opacity=0.8)
    p.M(self.xCenter, self.yCenter)
    for angle in range(0, int(20 * 3.14)):
      self.d.append(p)
      x = 10 * cos(angle)
      y = 10 * sin(angle)
      p.M(x + self.xCenter, y + self.yCenter)
    self.d.append(p)

##for (angle = 0; angle <= (2 * 3.14); angle += 0.01)
# {
#   x = R * cos(angle);
#   y = R * sin(angle);
#  glVertex3f(x + center.x, y + center.y, 0.0);
# if(i % 30 == 0)
#  randomiseColor();
# i++;
# }
##
