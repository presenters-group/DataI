from typing import List

from numpy import double, long
from DataI import enums
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel

import drawSvg as draw


class BarChart(PointChart):
    def __init__(self,  dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel, quality: double, animation: bool, nameFile):

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        super().__init__( dataSourceTableWithoutXcolumn, widthView, heightView,xcolumon, quality, animation, nameFile)
        self.widthOfSingleColumn = self.xUnit / (len(self.dataSourceTableWithoutXcolumn.columns)+2)
        self.drawColumns(dataSourceTableWithoutXcolumn.columnsColors)
        self.SVG = self.d.asSvg()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #self.d.saveSvg(nameFile + '.svg')

    def calculatWidthOfColumn(self) -> double:
      count = len(self.xColumn.cells)
      return double(25)

    def FindYofLeftEdgeOFCoulumn(self, index: int) -> double:
      return double(-index * self.widthOfSingleColumn)

    def FindYofRightEdgeOFCoulumn(self, index: int) -> double:
      return double(-(index + 1) * self.widthOfSingleColumn)

    def drawColumn(self,add,colors,columnCounter,j,cell):

      x = abs(add + self.FindYofRightEdgeOFCoulumn(j)) + self.widthOfSingleColumn
      y = abs(self.convertY(self.findZeroInSVG()))
      width = abs((add + self.FindYofRightEdgeOFCoulumn(j)) - (add + self.FindYofLeftEdgeOFCoulumn(j)))
      height = self.convertY(cell.value) - self.convertY(self.findZeroInSVG())
      if self.animation:
        if height > -1:
          t = draw.Rectangle(x, y + height, width, height, stroke=colors[columnCounter], stroke_width=self.xUnit / 60,
                            Class=str(self.Index), id=self.Index,

                            transform="rotate(180," + str(x) + ',' + str(-abs(y + height)) + ')',
                            fill=colors[columnCounter], fill_opacity=0.5)
          t.appendAnim(draw.Animate('height', '1s', from_or_values=0, to=height,

                                   repeatCount='1'))
          self.d.append(t)
        else:
          t = draw.Rectangle(x - self.widthOfSingleColumn, y - abs(height), width, abs(height), Class=str(self.Index),
                            id=self.Index,
                            stroke=colors[columnCounter],
                            stroke_width=self.xUnit / 30,
                            fill=colors[columnCounter], fill_opacity=0.5)
          t.appendAnim(draw.Animate('height', '1s', from_or_values=0, to=abs(height),

                                   repeatCount='1'))
          self.d.append(t)
      else:
        if height > -1:
          r = draw.Rectangle(x, y + height, width, height, stroke=colors[columnCounter], stroke_width=self.xUnit / 60,Class=str(self.Index),id=self.Index,
                           transform="rotate(180," + str(x) + ',' + str(-abs(y + height)) + ')',
                           fill=colors[columnCounter], fill_opacity=0.5)
          self.d.append(r)
        else:
          r = draw.Rectangle(x - self.widthOfSingleColumn, y - abs(height), width, abs(height),Class=str(self.Index),id=self.Index,
                           stroke=colors[columnCounter],
                           stroke_width=self.xUnit / 30,
                           fill=colors[columnCounter], fill_opacity=0.5)
          self.d.append(r)

    def drawColumns(self, colors: List[str]):
        columnCounter = 0
        j=-1
        for column in self.dataSourceTableWithoutXcolumn.columns:
          j+=1
          if column.columnType == enums.ColumnDataType.Measures.value:
            if column != self.xColumn:
                add = self.widthOfYLabels+self.xUnit + self.widthOfSingleColumn * (len(self.dataSourceTableWithoutXcolumn.columns)/2)
                if (column != self.xColumn):
                    for cell, i in zip(column.cells, range(0, len(self.xColumn.cells))):
                        if (i != 0):
                            name = str(column.name)
                            self.metaData.append(name+' = '+ str(cell.value))
                            self.drawColumn(add, colors, columnCounter, j, cell)
                            self.Index += 1
                            add += self.xUnit
          else:
              j -= 1

          columnCounter += 1
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def drawPointsOfValuesInDataSourceTableWithoutXColumn(self, colors: List[str]):
      print()
