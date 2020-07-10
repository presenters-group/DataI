import random
from typing import List
import drawSvg as draw
from numpy import double
from DataI.Models.ColumnModel import ColumnModel


class HumanChart:
    def __init__(self, firstcColumon: ColumnModel, secondColumn: ColumnModel, nameFile):
        self.widthView = 1000
        self.heightView = 1000
        self.firstColumn = firstcColumon
        self.secondColumn = secondColumn
        self.colorList = self.generateRandomColorsList(len(self.firstColumn.cells))
        self.listOfLength = list()
        self.d = draw.Drawing(self.widthView + 500, self.heightView)
        self.total = self.sumColumn(secondColumn)
        self.drawlayOut()
        self.drawStack()
        self.drawHuman()
        self.drawText()
        # self.d.saveSvg(nameFile+'.svg')
        self.SVG = self.d.asSvg()

    def drawHuman(self):

        p = draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                      d="M1008.5,989.9l-7.7-153.2c0,0-1.4-8.6-11.5-12.2c-10.1-3.6-262.8-172.1-262.8-172.1s-10.1-67-38.2-96.5	l16.6-76.3c0,0,22.3,14.4,25.9-9.4c3.6-23.8,20.2-106.6,3.6-118.1s-10.8-1.4-10.8-1.4s37.4-79.9-11.5-192.2c0,0-22.3-31-56.9-25.2	c0,0-30.2-36.7-121-20.9c0,0-39.6-11.5-41.8,18.7c0,0-49-3.6-83.5,97.9c0,0-17.3,56.9,33.1,133.2c0,0-38.2-6.5-25.2,23l14.4,95.8	c0,0,7.2,20.2,37.4,11.5l10.1,64.8c0,0-27.4,22.3-33.8,74.2L161.3,817.3c0,0-44.4,19.8-41.3,172.6l882.2,0.1h9.7H1300v110H0V0h1300	v990L1008.5,989.9z"
                      , transform="translate(0,-1000)")
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
        return double(((self.heightView - 100) / 100) * percent)

    def generateRandomColorsList(cls, listLength) -> List[str]:
        colorsList = []
        for i in range(listLength):
            random_color = random.randint(0, 16777215)
            hex_color = str(hex(random_color))
            hex_color = '#' + hex_color[2:]
            colorsList.append(hex_color)
        return colorsList

    def drawStack(self):
        oldstartPoint = 0
        height = 0
        startX = 0
        length = 0
        for cell, cell2, i in zip(self.firstColumn.cells, self.secondColumn.cells,
                                  range(0, len(self.firstColumn.cells))):
            if (type(cell2.value) != str):
                if (i != 0):
                    length += 1
                    startX += oldstartPoint
                    height = self.getLength(double(cell2.value))
                    oldstartPoint = height
                    self.d.append(
                        draw.Rectangle(0, startX, self.widthView + 50, height, fill=self.colorList[i], fill_opacity=0.5,
                                       stroke="white",
                                       stroke_width=2))

    def drawText(self):
        oldstartPoint = 0
        startX = 0
        length = 0
        for cell, cell2, i in zip(self.firstColumn.cells, self.secondColumn.cells,
                                  range(0, len(self.firstColumn.cells))):
            if (type(cell2.value) != str):
                if (i != 0):
                    length += 1
                    startX += oldstartPoint
                    height = self.getLength(double(cell2.value))
                    oldstartPoint = height
                    text = str(cell.value) + ": " + str(self.percentageOfValue(double(cell2.value)))[0:4] + "%"
                    self.d.append(
                        draw.Circle(self.widthView + 100, length * 80, 20, fill=self.colorList[i], fill_opacity=0.5,
                                    stroke_width=0))
                    self.d.append(draw.Text(text=str(text), fontSize=30, x=self.widthView + 150, y=length * 80 - 10))
