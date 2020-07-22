from typing import List

import drawSvg as draw

from numpy import double, long
from DataI import enums
from DataI.Controllers.DrawControllers.chart import Chart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class PointChart(Chart):
    def __init__(self, dataSourceTableWithoutXcolumn: TableModel, widthView: double, heightView: double,
                 xcolumon: ColumnModel, quality: double, animation: bool, nameFile):
        super().__init__(dataSourceTableWithoutXcolumn, widthView, heightView, xcolumon, animation)
        # if(len(xcolumon.cells)>50):
        #   widthView = 10*len(xcolumon.cells)
        self.widthOfYLabels = widthView / 8
        self.heightOfXLabels = heightView / 8
        self.widthOfCoordinatePlane = self.widthView - self.widthOfYLabels
        self.heightOfCoordinatePlane = self.heightView - self.heightOfXLabels
        self.widthView -= self.widthOfYLabels/2
        self.heightView -= self.heightOfXLabels/2
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
        self.drawXPointsWithXValueSteps()
        self.drawPointsOfValuesInDataSourceTableWithoutXColumn(dataSourceTableWithoutXcolumn.columnsColors)
        self.drawColmunsColorList(dataSourceTableWithoutXcolumn.columnsColors)
        self.drawSideLable()
        #self.d.setPixelScale(100000)  # Set number of pixels per geometry unit
        #self.d.saveSvg(nameFile + '.svg')
        #    self.d.savePng(nameFile+'.png')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView, self.heightView, fill='#ffffff'))

    def findStartYvalue(self):
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value and column != self.xColumn:
              return double( column.cells[1].value)
            # else:
            #   for column in self.dataSourceTableWithoutXcolumn.columns:
            #     print(column.name)
            #   print("name:",column.name)
            #   print("column.columnType == enums.ColumnDataType.Measures.value:",column.columnType == enums.ColumnDataType.Measures.value)
            #   print("column != self.xColumn:",column != self.xColumn)
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
            if column.columnType == enums.ColumnDataType.Measures.value and column != self.xColumn:
                for cell in column.cells:
                    if (cell.type == enums.CellType.numeric.value):
                        if (double(cell.value) > Max):
                            Max = double(cell.value)
        return Max

    def findMinimumValue(self):
        min = self.findStartYvalue()
        for column in self.dataSourceTableWithoutXcolumn.columns:
            if column.columnType == enums.ColumnDataType.Measures.value and column != self.xColumn:
                for cell in column.cells[1:]:
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
            p = draw.Path(stroke_width=self.heightOfCoordinatePlane / 250, stroke='lightgray', fill='gray', fill_opacity=0)
            p.M(self.widthOfYLabels, self.convertY(self.listOfLevelXValue[i]))
            p.h(self.widthOfCoordinatePlane)
            self.d.append(p)
            y += self.yStep

    def drawPointsOfValuesInDataSourceTableWithoutXColumn(self, colors: List[str]):
        columnCounter = 0
        for column in self.dataSourceTableWithoutXcolumn.columns:
          if column.columnType == enums.ColumnDataType.Measures.value:
            if (column != self.xColumn):
                # print(column.columnType)
                add = self.widthOfYLabels
                for cell, i in zip(column.cells, range(0, len(self.xColumn.cells))):
                    if (i != 0):
                        add += self.xUnit
                        self.metaData.append("(" + str(self.xColumn.cells[i].value) + "," + str(cell.value) + ")")
                        self.d.append(draw.Circle(add, self.convertY(double(cell.value)), self.xUnit / 30,
                                                  fill=colors[column.id],
                                                  stroke_width=0,Class=str(self.Index),
                                                  stroke='black', id=(self.Index)))
                        self.Index += 1

            columnCounter += 1

    def drawXPointsWithXValueSteps(self):
        add = self.widthOfYLabels
        for cell, i in zip(self.xColumn.cells[0:], range(1, len(self.xColumn.cells))):
            add += self.xUnit
            num = self.xColumn.cells[i].value
            self.metaData.append(str(num))
            if (len(str(num)) > 10):
                num = num[0:8] + "..."
            self.d.append(
                draw.Circle(add, self.heightOfXLabels, self.xUnit / 35, fill="black", stroke_width=0, stroke='black'))
            self.d.append(
                draw.Text(text=str(num), fontSize=self.heightOfXLabels /10, x=add ,
                          y=self.heightOfXLabels /1.29,
                          id=str(self.Index),Class=str(self.Index),
                          style="font-size : " + str(self.heightOfXLabels / 10),
                          transform="rotate(90," + str(add ) + "," + str(-self.heightOfXLabels / 1.29) + ")"))
            self.Index += 1

    def drawColmunsColorList(self, colors: List[str]):
        if((self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 1)) / 15 <(self.heightView / (len(self.dataSourceTableWithoutXcolumn.columns) + 1)) / 15):
          fontSize = (self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 1)) / 15
        else:
          fontSize = (self.heightView / (len(self.dataSourceTableWithoutXcolumn.columns) + 1)) / 15
        add = self.widthView / 50
        num = "X:" + str(self.xColumn.name)
        if (len(str(num)) > 10):
            num = num[0:8] + "..."
        self.metaData.append("X:" + str(self.xColumn.name))
        self.Index += 1
        self.d.append(draw.Circle(add, self.heightOfXLabels / 4 +(fontSize / 2), fontSize / 2, fill="black", stroke_width=0,
                                  stroke='black',fill_opacity=1))
        self.d.append(
            draw.Text(text=str(num), fontSize=fontSize, x=add + (fontSize * 2),
                      y=self.heightOfXLabels / 4 + (fontSize / 3),style="font-size : " + str(fontSize),
                      Class=str(self.Index),id=str(self.Index)))
        add += self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 3)


        columnCounter = 0
        for column in self.dataSourceTableWithoutXcolumn.columns:
          if column !=self.xColumn:
            if column.columnType == enums.ColumnDataType.Measures.value:
                num = column.name
                if (len(str(num)) > 10):
                    num = num[0:8] + "..."
                self.metaData.append(num)
                self.d.append(
                    draw.Circle(add, self.heightOfXLabels / 4 + (fontSize / 2), fontSize / 2, fill=colors[columnCounter],
                                stroke_width=0,
                                stroke='black'))
                self.d.append(draw.Text(text=str(num), fontSize=fontSize, x=add + (fontSize * 2),
                                        y=self.heightOfXLabels / 4 + (fontSize / 3),style="font-size : " +str(fontSize),
                                        Class=str(self.Index),id=str(self.Index)))
                add += self.widthView / (len(self.dataSourceTableWithoutXcolumn.columns) + 3)
                self.Index += 1
          columnCounter += 1

    def drawSideLable(self):
        fontSize = self.widthOfYLabels/8
        if( self.widthOfYLabels/8 > (self.heightOfCoordinatePlane/self.quality)/8):
          fontSize =  (self.heightOfCoordinatePlane/self.quality)/8
        y = self.heightOfXLabels
        x = self.widthOfYLabels / 10
        for i in range(0, int(self.quality)):
            num = str(self.listOfLevelXValue[i])
            self.metaData.append(num)
            if (len(num) > 10):
                num = num[0:8] + "..."
            self.d.append(
                draw.Text(text=str(num), fontSize=fontSize, x=x,
                          y=self.convertY(self.listOfLevelXValue[i]),style="font-size : "+str(fontSize),
                          Class=str(self.Index),id=str(self.Index)))
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
