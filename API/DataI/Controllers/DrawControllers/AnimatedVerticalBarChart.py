from typing import List

from numpy import double, long
from DataI import enums
from DataI.Controllers.DrawControllers.BarChart import BarChart
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel

import drawSvg as draw


class AnimatedVerticalBarChart(BarChart):
    def __init__(self,  dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel, quality: double, nameFile):

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        super().__init__( dataSourceTableWithoutXcolumn, widthView, heightView,xcolumon, quality, nameFile)
        self.SVG = self.d.asSvg()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #self.d.saveSvg(nameFile + '.svg')

    def drawColumn(self,add,colors,columnCounter,j,cell):
      x = abs(add + self.FindYofRightEdgeOFCoulumn(j)) + self.widthOfSingleColumn
      y = abs(self.convertY(self.findZeroInSVG()))
      width = abs((add + self.FindYofRightEdgeOFCoulumn(j)) - (add + self.FindYofLeftEdgeOFCoulumn(j)))
      height = self.convertY(cell.value) - self.convertY(self.findZeroInSVG())
      if height > -1:
        r = draw.Rectangle(x, y + height, width, height, stroke=colors[columnCounter], stroke_width=self.xUnit / 60,id=self.Index,
                           transform="rotate(180," + str(x) + ',' + str(-abs(y + height)) + ')',
                           fill=colors[columnCounter], fill_opacity=0.5)
        r.appendAnim(draw.Animate('height', '1s', from_or_values=0, to=height,

                                  repeatCount='1'))
        self.d.append(r)
      else:
        r = draw.Rectangle(x - self.widthOfSingleColumn, y - abs(height), width, abs(height),id=self.Index,
                           stroke=colors[columnCounter],
                           stroke_width=self.xUnit / 30,
                           fill=colors[columnCounter], fill_opacity=0.5)
        r.appendAnim(draw.Animate('height', '1s', from_or_values=0, to=abs(height),

                                  repeatCount='1'))
        self.d.append(r)
