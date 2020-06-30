import random
import drawSvg as draw
import numpy as np

from typing import List
from numpy import double
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class MultiplePieChart:
  def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, nameFile):
    self.widthView = width
    self.heightView = height
    self.data = dataSource
    self.xColumn = XColumn
    self.r = min(width, height) / 2
    self.d = draw.Drawing(self.widthView + 500, self.heightView + 100)
    self.total = self.sumColumn(XColumn)
    self.xCenter = min(width + 100, height + 100) / 2
    self.yCenter = - min(width + 100, height + 100) / 2
    self.drawlayOut()
    self.drawCircle()
    #self.d.saveSvg(nameFile + '.svg')
    self.SVG = self.d.asSvg()

  def drawlayOut(self):
    self.d.append(draw.Rectangle(0, 0, self.widthView + 500, self.heightView + 100, fill='#ffffff'))

  def sumColumn(self, column: ColumnModel) -> double:
    sum = 0.0
    for cell, i in zip(column.cells, range(0, len(column.cells))):
      if (type(cell.value) != str):
        if (i != 0):
          sum += abs(cell.value)
    return double(sum)

  def percentageOfValue(self, value: double, column: ColumnModel) -> double:
    return double((abs(value) / self.sumColumn(column)) * 100)

  def getAngle(self, value: double, column: ColumnModel) -> int:
    percent = self.percentageOfValue(value, column)
    return double((360 / 100) * percent)

  def generateRandomColorsList(cls, listLength) -> List[str]:
    colorsList = []

    for i in range(listLength):
      random_color = random.randint(0, 16777215)
      hex_color = str(hex(random_color))
      hex_color = '#' + hex_color[2:]
      colorsList.append(hex_color)

    return colorsList

  def drawCircle(self):
    colorList = self.generateRandomColorsList(int(len(self.xColumn.cells)))
    xCenter = self.xCenter
    yCenter = self.yCenter
    # ========================================================================
    x = self.r / (len(self.data.columns))
    r = self.r + x
    # ================================================================
    for column in self.data.columns:
      if (column != self.xColumn):
        print("Before:", r)
        r -= (x)
        print("after:", r)
        oldEndangle = 0
        endAngle = 0
        length = 0
        b = 0
        # self.d.append(draw.Circle(-self.yCenter, self.xCenter, lngth, fill="white", fill_opacity=1, stroke_width=0,stroke="black"))
        for cell, cell2, i in zip(self.xColumn.cells, column.cells, range(0, len(self.xColumn.cells))):
          if (i != 0):

            length += 1
            startangle = oldEndangle
            endAngle += self.getAngle(double(cell2.value), column)
            oldEndangle = endAngle
            radiansconversion = np.pi / 180.
            xstartpoint = xCenter + r * np.cos(startangle * radiansconversion)
            ystartpoint = yCenter - r * np.sin(startangle * radiansconversion)
            xendpoint = xCenter + r * np.cos(endAngle * radiansconversion)
            yendpoint = yCenter - r * np.sin(endAngle * radiansconversion)
            large_arc_flag = 0
            if endAngle - startangle > 180: large_arc_flag = 1
            M = ("M %s %s" % (xstartpoint, ystartpoint))
            a = ("A %s %s 0 %s 0 %s %s" % (r, r, large_arc_flag, xendpoint, yendpoint))
            L = ("L %s %s" % (xCenter, yCenter))
            p = draw.Path(stroke_width=10, stroke="white", fill=colorList[i - 1], fill_opacity=1, d=M + a + L)
            p.Z()
            self.d.append(p)
            if (b == 0):
              text = str(cell.value)
              self.d.append(draw.Circle(self.widthView + 100, length * 80, 20, fill=colorList[i - 1], fill_opacity=1,
                                        stroke_width=0))
              self.d.append(draw.Text(text=str(text), fontSize=30, x=self.widthView + 150, y=length * 80 - 10))
            print("Before:", r)

        b += 1
