import drawSvg as draw
import numpy as np

from numpy import double
from DataI.Controllers.DrawControllers.PieChart import PieChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class SmartPieChart(PieChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str):
      self.Index = 0
      self.metaData = list()
      self.colorList = dataSource.rowsColors
      super().__init__(dataSource.columns[0], XColumn, double(1000), double(1000), animation, nameFile)
      self.d.setPixelScale(min(width, height) / 1000)  # Set number of pixels per geometry unit
      self.SVG = self.d.asSvg()
      #self.d.saveSvg(nameFile + '.svg')

    def drawCircle(self):

        xcenter = self.xCenter
        ycenter = self.yCenter
        r = self.r
        Y = -self.yCenter
        length = 0
        for cell, cell2, i in zip(self.firstColumn.cells, self.secondColumn.cells,
                                  range(0, len(self.firstColumn.cells))):
            if (type(cell2.value) != str):
                if (i != 0):
                    length += 1
                    startangle = 0
                    endangle = self.getAngle(double(cell2.value))
                    radiansconversion = np.pi / 180.
                    xstartpoint = xcenter + r * np.cos(startangle * radiansconversion)
                    ystartpoint = ycenter - r * np.sin(startangle * radiansconversion)
                    xendpoint = xcenter + r * np.cos(endangle * radiansconversion)
                    yendpoint = ycenter - r * np.sin(endangle * radiansconversion)
                    large_arc_flag = 0
                    if endangle - startangle > 180: large_arc_flag = 1
                    M = ("M %s %s" % (xstartpoint, ystartpoint))
                    a = ("A %s %s 0 %s 0 %s %s" % (r, r, large_arc_flag, xendpoint, yendpoint))
                    L = ("L %s %s" % (xcenter, ycenter))
                    p = draw.Path(stroke_width=10, stroke="white", fill=self.colorList[i - 1], fill_opacity=1,
                                  d=M + a + L,Class=str(self.Index),id=self.Index)


                    p.Z()
                    self.d.append(p)
                    text = str(self.firstColumn.cells[i - len(self.firstColumn.cells)].value) + ": " + str(
                        self.percentageOfValue(cell2.value))[0:4] + "%"
                    self.metaData.append(text)
                    r -= self.r / len(self.firstColumn.cells)
                    self.d.append(
                        draw.Circle(-ycenter, xcenter, r, fill="white", fill_opacity=1,
                                    stroke="white", stroke_width=10))
                    self.d.append(draw.Text(text=str(text), fontSize=50, x=str((length * 55 + 8) - 50), y=Y - 5, style="font-size : "+str(50),
                                            transform="rotate(90," + str(self.xCenter - 40) + "," + str(
                                                -length * 55 + 8) + ")",Class=str(self.Index),id=self.Index))
                    self.Index += 1
                    Y -= (self.r / len(self.firstColumn.cells)) / 8
