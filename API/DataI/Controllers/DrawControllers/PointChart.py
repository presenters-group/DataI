import drawSvg as draw

from numpy import double, long
from DataI import enums
from DataI.Controllers.DrawControllers.chart import Chart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class PointChart(Chart):
    def __init__(self, dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel, quality: double, nameFile):
        super().__init__(dataSourceTableWithoutXcolumn, widthView, heightView, xcolumon)
        self.listOfIndexing = list()
        self.Index = 0
        self.widthOfYLabels = self.widthView / 8
        self.heightOfXLabels = self.heightView / 5
        self.widthOfCoordinatePlane = self.widthView
        self.heightOfCoordinatePlane = self.heightView
        self.widthView += self.widthOfYLabels
        self.heightView += self.heightOfXLabels
        self.quality = quality
        self.d = draw.Drawing(self.widthView, self.heightView)
        self.listOfLevelXValue = list()
        self.drawlayOut()
        self.maximumValue = self.findMaximumValue()
        self.minimumValue = self.findMinimumValue()
        self.yDistance = self.getDistant()
        self.yUnit = self.getyUnit()
        self.xUnit = self.getxUnit()
        self.yStep = self.getYstep()
        self.yUnit = self.correctingUnit()
        self.getYLevelsValue()
        self.startValue = self.listOfLevelXValue[0]
        self.drawYLineLevels()
        self.drawPointsOfValuesInDataSourceTableWithoutXColumn()
        self.drawXPointsWithXValueSteps()
        self.drawColmunsColorList()
        self.drawSideLable()
        self.d.setPixelScale(1)  # Set number of pixels per geometry unit
        # self.d.setRenderSize(400,200)
        # self.d.saveSvg(nameFile + '.svg')
        #    self.d.savePng(nameFile+'.png')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView, self.heightView, fill='#ffffff'))

    def findStartYvalue(self):
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if (column.columnType == enums.ColumnDataType.Measures.value):
                for cell in column.cells[1:]:
                    return double(cell.value)
        return 0

    def getStartvalue(self) -> double:
        num = 0
        if (len(self.listOfLevelXValue) != 0):
            num = self.listOfLevelXValue[0]
            for value in self.listOfLevelXValue:
                if (value == 0):
                    num = 0
        return num

    def findMaximumValue(self):
        Max = self.findStartYvalue()
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value:
                for cell in column.cells:
                    if (cell.type == enums.CellType.numeric.value):
                        if (double(cell.value) > Max):
                            Max = double(cell.value)
        return Max

    def findMinimumValue(self):
        min = self.findStartYvalue()
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value:
                for cell in column.cells:
                    if (cell.type == enums.CellType.numeric.value):
                        if (double(cell.value) < min):
                            min = double(cell.value)
        return min

    def getDistant(self):
        if (self.maximumValue == self.minimumValue):
            return self.maximumValue
        return self.maximumValue - self.minimumValue

    def getyUnit(self) -> double:
        return double(self.yDistance / (self.quality - 2))

    def getxUnit(self) -> double:
        return double(self.widthOfCoordinatePlane / (len(self.xColumn.cells)))

    def getYstep(self) -> double:
        return double(self.heightOfCoordinatePlane / (self.quality))

    def correctingUnit(self):
        integer = long(self.yUnit)
        beforeTheComma = self.yUnit - integer
        t = long(beforeTheComma * 100)
        t = self.getCloseNumber(t) / 100
        return integer + t

    def getLastLevel(self, min: double, unit: double) -> double:
        i = 0
        level = 0
        while (double(level) > min):
            i += 1
            level -= unit
        self.minimumValue = level
        return double(level)

    def getYLevelsValue(self):
        if ((self.minimumValue < 0) & (self.maximumValue > 0)):
            min = self.getLastLevel(double(self.minimumValue), self.yUnit)
            for i in range(0, int(self.quality)):
                self.listOfLevelXValue.append(min)
                min += self.yUnit
        else:
            for i in range(0, int(self.quality)):
                self.listOfLevelXValue.append(double(self.minimumValue))
                self.minimumValue += self.yUnit

    def convertY(self, value) -> double:
        return double(((value - self.startValue) * self.yStep) / self.yUnit + self.heightOfXLabels)

    def drawYLineLevels(self):
        y = self.heightOfXLabels
        for i in range(0, int(self.quality)):
            p = draw.Path(stroke_width=self.yUnit / 75, stroke='lightgray', fill='gray', fill_opacity=0)
            p.M(self.widthOfYLabels, self.convertY(self.listOfLevelXValue[i]))
            p.h(self.widthOfCoordinatePlane)
            self.d.append(p)
            y += self.yStep

    def drawPointsOfValuesInDataSourceTableWithoutXColumn(self):
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value:
                print(column.columnType)
                add = self.widthOfYLabels
                for cell, i in zip(column.cells, range(0, len(self.xColumn.cells))):
                    if (i != 0):
                        add += self.xUnit
                        self.listOfIndexing.append("(" + str(self.xColumn.cells[i].value) + "," + str(cell.value) + ")")
                        self.d.append(draw.Circle(add, self.convertY(double(cell.value)), self.xUnit / 20,
                                                  fill=column.style.color,
                                                  stroke_width=0,
                                                  stroke='black', id=(self.Index)))
                        self.Index += 1

    def drawXPointsWithXValueSteps(self):
        add = self.widthOfYLabels
        for cell, i in zip(self.xColumn.cells[1:], range(0, len(self.xColumn.cells))):
            add += self.xUnit
            num = self.xColumn.cells[i].value
            self.listOfIndexing.append(str(num))
            if (len(str(num)) > 10):
                num = num[0:8] + "..."
            self.d.append(
                draw.Circle(add, self.heightOfXLabels, self.xUnit / 25, fill="black", stroke_width=0, stroke='black'))
            self.d.append(
                draw.Text(text=str(num), fontSize=self.heightOfXLabels / 15, x=add - (self.heightOfXLabels / 10),
                          y=self.heightOfXLabels / 1.3 - (self.xUnit / 5) / 5,
                          id=str(self.Index),
                          transform="rotate(90," + str(add - 1) + "," + str(-self.heightOfXLabels / 1.3) + ")"))
            self.Index += 1

    def drawColmunsColorList(self):
        fontSize = (self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 1)) / 10
        add = self.widthView / 50
        num = "X:" + str(self.xColumn.name)
        if (len(str(num)) > 10):
            num = num[0:8] + "..."
        self.d.append(draw.Circle(add, self.heightOfXLabels / 4 + 8, fontSize / 2, fill="black", stroke_width=0,
                                  stroke='black'))
        self.d.append(
            draw.Text(text=str(num), fontSize=fontSize, x=add + (fontSize * 2),
                      y=self.heightOfXLabels / 4 + (fontSize / 2),
                      id=str(self.Index)))
        add += self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 3)
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value:
                num = column.name
                if (len(str(num)) > 10):
                    num = num[0:8] + "..."
                self.d.append(
                    draw.Circle(add, self.heightOfXLabels / 4 + 8, fontSize / 2, fill=column.style.color,
                                stroke_width=0,
                                stroke='black'))
                self.d.append(draw.Text(text=str(num), fontSize=fontSize, x=add + (fontSize * 2),
                                        y=self.heightOfXLabels / 4 + (fontSize / 2),
                                        id=str(self.Index)))
                add += self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 3)

    def drawSideLable(self):
        y = self.heightOfXLabels
        x = self.widthOfYLabels / 10
        for i in range(0, int(self.quality)):
            num = str(self.listOfLevelXValue[i])
            self.listOfIndexing.append(num)
            if (len(num) > 10):
                num = num[0:8] + "..."
            self.d.append(
                draw.Text(text=str(num), fontSize=self.widthOfYLabels / 8, x=x,
                          y=self.convertY(self.listOfLevelXValue[i]),
                          id=str(self.Index)))
            self.Index += 1

    def getXPointlInSVG(self, i: int) -> double:
        return double((i * self.xUnit) + self.widthOfYLabels)

    def getCloseNumber(self, num) -> double:
        temp = num % 10
        num -= temp
        if (temp < 5):
            num += 5
        else:
            num += 10
        return num

    def findZeroInSVG(self) -> double:
        for value in self.listOfLevelXValue:
            if (long(value) == 0):
                return double(0)
        return self.listOfLevelXValue[0]

    #######################################################################################################
