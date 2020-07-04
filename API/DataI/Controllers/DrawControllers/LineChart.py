import drawSvg as draw

from numpy import double
from DataI import enums
from DataI.Controllers.DrawControllers.PointChart import PointChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class LineChart(PointChart):
    def __init__(self, dataSource: TableModel, width: double, height: double, Xcolomn: ColumnModel, quality: double,
                 nameFile):
        super().__init__(dataSource, width, height, Xcolomn, quality, nameFile)
        self.drawLines()
        self.d.saveSvg(nameFile + '.svg')
        self.d.savePng(nameFile + '.png')
        self.SVG = self.d.asSvg()

    def drawLines(self):
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value:
                add = self.widthOfYLabels
                p = draw.Path(stroke_width=self.xUnit / 50, stroke=column.style.color,
                              fill=column.style.color, fill_opacity=0, id=str(self.Index))
                name = str(column.name)
                self.listOfIndexing.append(name)
                self.Index += 1
                p.M(add, self.convertY(self.findZeroInSVG()))
                if (column != self.xColumn):
                    for cell, i in zip(column.cells, range(0, len(self.xColumn.cells))):
                        print(cell)
                        if (i != 0):
                            add += self.xUnit
                            p.L(add, self.convertY(double(cell.value)))
                p.V(self.convertY(self.findZeroInSVG()))
                self.d.append(p)
