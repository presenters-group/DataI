import random
from typing import List

import drawSvg as draw
from numpy import double

from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class PyramidalChart:
  def __init__(self, firstcColumon: TableModel, secondColumn: ColumnModel, width: double, height: double, nameFile):
    self.widthView = width
    self.heightView = height
    self.firstColumn = firstcColumon.columns[0]
    self.secondColumn = secondColumn
    self.listOfLength = list()
    self.d = draw.Drawing(self.widthView + 300, self.heightView + 100)
    self.total = self.sumColumn(secondColumn)
    self.drawlayOut()
    self.drawStack()
    self.drawPyramidal()
    self.d.saveSvg(nameFile + '.svg')
    self.SVG = self.d.asSvg()

  def drawPyramidal(self):
    p = draw.Path(stroke_width=0, stroke="gray",
                  fill="white", fill_opacity=1)
    p.M(0, 50)
    p.V(self.heightView + 50)
    p.H((self.widthView - 100) / 2)
    p.Z()
    self.d.append(p)
    p = draw.Path(stroke_width=0, stroke="gray",
                  fill="white", fill_opacity=1)
    p.M(self.widthView - 100, 50)
    p.V(self.heightView + 50)
    p.H((self.widthView - 100) / 2)
    p.Z()
    self.d.append(p)

  def drawlayOut(self):
    self.d.append(draw.Rectangle(0, 0, self.widthView + 500, self.heightView + 100, fill='#ffffff'))

  def sumColumn(self, column: ColumnModel) -> double:
    sum = 0.0
    for cell, i in zip(column.cells, range(0, len(column.cells))):
      if (type(cell.value) != str):
        if (i != 0):
          sum += abs(cell.value)
    return double(sum)

  def percentageOfValue(self, value: double) -> double:
    return double((abs(value) / self.total) * 100)

  def getLength(self, value: double) -> double:
    percent = self.percentageOfValue(value)
    return double((self.heightView / 100) * percent)

  def generateRandomColorsList(cls, listLength) -> List[str]:
    colorsList = []
    for i in range(listLength):
      random_color = random.randint(0, 16777215)
      hex_color = str(hex(random_color))
      hex_color = '#' + hex_color[2:]
      colorsList.append(hex_color)
    return colorsList

  def drawStack(self):
    colorList = self.generateRandomColorsList(len(self.firstColumn.cells))
    oldstartPoint = 0
    height = 0
    startX = 50
    length = 0
    for cell, cell2, i in zip(self.firstColumn.cells, self.secondColumn.cells, range(0, len(self.firstColumn.cells))):
      if (type(cell2.value) != str):
        if (i != 0):
          length += 1
          startX += oldstartPoint
          height = self.getLength(double(cell2.value))
          oldstartPoint = height
          self.d.append(
            draw.Rectangle(0, startX, self.widthView - 100, height, fill=colorList[i], fill_opacity=0.5, stroke="white",
                           stroke_width=5))
          text = str(cell.value) + ": " + str(self.percentageOfValue(double(cell2.value)))[0:4] + "%"
          self.d.append(
            draw.Circle(self.widthView, length * 80, 20, fill=colorList[i], fill_opacity=0.5, stroke_width=0))
          self.d.append(draw.Text(text=str(text), fontSize=30, x=self.widthView + 50, y=length * 80 - 10))
