import random
import drawSvg as draw
import numpy as np

from typing import List
from numpy import double

from DataI import enums
from DataI.Models.ColumnModel import ColumnModel


class PieChart():
    def __init__(self, firstColumn: ColumnModel, secondColumn: ColumnModel, width: double, height: double, animation: bool, nameFile):
        self.animation = animation
        self.widthView = width
        self.heightView = height
        self.firstColumn = firstColumn
        self.secondColumn = secondColumn
        self.r = min(width, height) / 2
        self.d = draw.Drawing(self.widthView + 100, self.heightView + 100)
        self.total = self.sumColumn(secondColumn)
        self.xCenter = min(width + 100, height + 100) / 2
        self.yCenter = - min(width + 100, height + 100) / 2
        self.drawlayOut()
        if self.secondColumn.columnType == enums.ColumnDataType.Measures.value:
          self.drawCircle()
        else:
          self.d.append(draw.Text(text="Error: Xcolumn is not Measured", fontSize=60, x=50, y=self.heightView/2))

        # self.d.saveSvg(nameFile + '.svg')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView + 100, self.heightView + 100, fill='#ffffff'))

    def sumColumn(self, column: ColumnModel) -> double:
        sum = 0.0
        for cell, i in zip(column.cells, range(0, len(column.cells))):
            if (type(cell.value) != str):
                if (i != 0):
                    sum += abs(cell.value)
        return double(sum)

    def percentageOfValue(self, value: double) -> double:
        return double((abs(value) / self.total) * 100)

    def getAngle(self, value: double) -> int:
        percent = self.percentageOfValue(value)
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
        colorList = self.generateRandomColorsList(len(self.firstColumn.cells))
        xCenter = self.xCenter
        yCenter = self.yCenter
        r = self.r
        oldEndangle = 0
        endAngle = 0
        length = 0
        for cell, cell2, i in zip(self.firstColumn.cells, self.secondColumn.cells,
                                  range(0, len(self.firstColumn.cells))):
            if (type(cell2.value) != str):
                if (i != 0):
                    length += 1
                    startangle = oldEndangle
                    endAngle += self.getAngle(double(cell2.value))
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
                    p = draw.Path(stroke_width=10, stroke="white", fill=colorList[i - 1], fill_opacity=0.5, d=M + a + L)
                    p.Z()
                    self.d.append(p)
                    text = str(cell.value) + ": " + str(self.percentageOfValue(double(cell2.value)))[0:4] + "%"
                    self.d.append(
                        draw.Circle(self.widthView + 100, length * 80, 20, fill=colorList[i - 1], fill_opacity=0.5,
                                    stroke_width=0))
                    self.d.append(draw.Text(text=str(text), fontSize=30, x=self.widthView + 150, y=length * 80 - 10))

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
