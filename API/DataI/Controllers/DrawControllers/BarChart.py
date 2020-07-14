from typing import List

from numpy import double, long
from DataI import enums
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel

import drawSvg as draw


class BarChart(PointChart):
    def __init__(self,  dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel, quality: double, nameFile):

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        super().__init__( dataSourceTableWithoutXcolumn, widthView, heightView,xcolumon, quality, nameFile)
        self.widthOfSingleColumn = self.xUnit / (len(self.dataSourceTableWithoutXcolumn.columns)+2)
        print("widthhhhhhhhhhhhh:",self.widthOfSingleColumn)
        self.drawColumns(dataSourceTableWithoutXcolumn.columnsColors)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        print(nameFile)
        self.d.saveSvg(nameFile + '.svg')

    def calculatWidthOfColumn(self) -> double:
      count = len(self.xColumn.cells)
      return double(25)

    def FindYofLeftEdgeOFCoulumn(self, index: int) -> double:
      return double(-index * self.widthOfSingleColumn)

    def FindYofRightEdgeOFCoulumn(self, index: int) -> double:
      return double(-(index + 1) * self.widthOfSingleColumn)

    def drawColumns(self, colors: List[str]):
        columnCounter = 0
        j=-1
        for column in self.dataSourceTableWithoutXcolumn.columns:
          j+=1
          if column.columnType == enums.ColumnDataType.Measures.value:
            if column != self.xColumn:
                add = self.widthOfYLabels+self.xUnit + self.widthOfSingleColumn * (len(self.dataSourceTableWithoutXcolumn.columns)/2)
                name = str(column.name)
                self.listOfIndexing.append(name)
                self.Index += 1
                if (column != self.xColumn):
                    for cell, i in zip(column.cells, range(0, len(self.xColumn.cells))):
                        if (i != 0):
                            p = draw.Path(stroke_width=self.xUnit / 50, stroke=colors[columnCounter],
                                        fill=colors[columnCounter], fill_opacity=0.5, id=str(self.Index))
                            p.M(add+self.FindYofLeftEdgeOFCoulumn(j), self.convertY(self.findZeroInSVG()))
                            p.V(self.convertY(cell.value))
                            p.H(add+self.FindYofRightEdgeOFCoulumn(j))
                            p.L(add+self.FindYofRightEdgeOFCoulumn(j), self.convertY(self.findZeroInSVG()))
                            self.d.append(p)
                            add += self.xUnit
            columnCounter += 1
          else:
              j -= 1
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def drawPointsOfValuesInDataSourceTableWithoutXColumn(self, colors: List[str]):
      print()
