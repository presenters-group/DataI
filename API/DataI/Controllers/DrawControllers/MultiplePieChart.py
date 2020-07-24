import random
import drawSvg as draw
import numpy as np

from typing import List
from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.chart import Chart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class MultiplePieChart(Chart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str):
        super().__init__(dataSource, width, height, XColumn, animation)
        width -= width/4
        self.r = (min(width, height) / 2)/1.1
        self.stroke = self.r /50
        self.d = draw.Drawing(self.widthView , self.heightView )
        self.total = self.sumColumn(XColumn)
        self.xCenter = width/ 2
        self.yCenter = - height/ 2
        self.drawlayOut()
        self.drawCircle()

        #self.d.saveSvg(nameFile + '.svg')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView, self.heightView, fill='#ffffff'))

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
        colorList = self.dataSourceTableWithoutXcolumn.rowsColors
        xCenter = self.xCenter
        yCenter = self.yCenter
        # ========================================================================
        x = self.r / (len(self.dataSourceTableWithoutXcolumn.columns))
        r = self.r + x
        # ================================================================
        for column in self.dataSourceTableWithoutXcolumn.columns:
          if column.columnType == enums.ColumnDataType.Measures.value:
            if (column != self.xColumn):
                r -= (x)
                oldEndangle = 0
                endAngle = 0
                length = 0
                b = 0
                for cell, cell2, i in zip(self.xColumn.cells, column.cells, range(0, len(self.xColumn.cells))):
                    if (i != 0):
                        length += self.heightView /len(self.xColumn.cells)
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
                        p = draw.Path(stroke_width=self.stroke, stroke="white", fill=colorList[i - 1], fill_opacity=1,
                                      d=M + a + L)
                        p.Z()
                        self.d.append(p)
                        if (b == 0):
                            text = str(cell.value)
                            c=draw.Circle(self.widthView - self.widthView/4.5, length , self.stroke*2, fill=colorList[i - 1],fill_opacity=1,stroke_width=0)
                            t=draw.Text(text=str(text), fontSize=self.stroke*4,style="font-size :"+str(self.stroke*4),x=self.widthView - self.widthView/6, y=length-length/50)
                            if self.animation:
                              t.appendAnim(draw.Animate('x', str((length / 150)-0.2) + 's', from_or_values=0, to=self.widthView - self.widthView/6,repeatCount='1'))
                              c.appendAnim(draw.Animate('cx', str(length / 150) + 's', from_or_values=0, to=self.widthView - self.widthView/4.5,repeatCount='1'))
                              c.appendAnim(draw.Animate('r', '3.2s', from_or_values=self.stroke*2*5, to=abs(self.stroke*2), repeatCount='1'))

                            self.d.append(t)
                            self.d.append(c)


                b += 1
