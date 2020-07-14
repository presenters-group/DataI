import random
from typing import List
import drawSvg as draw
from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Controllers.DrawControllers.chart import Chart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class FemaleAndMaleChart(InfChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, nameFile: str):
      super().__init__(dataSource, XColumn,width, height, nameFile)
      self.maleColumn = self.femaleColumn = XColumn
      self.getMaleAndFemaleColumns()
      self.drawMaleAndFemaleStack()
      self.drawHuman()
      self.drawText()
      self.d.setPixelScale(min(width, height) / 1000)  # Set number of pixels per geometry unit
      #self.d.saveSvg(nameFile + '.svg')
      self.SVG = self.d.asSvg()


    def getMaleAndFemaleColumns(self):
        for column in self.dataSourceTableWithoutXcolumn.columns:
          if column.name == "male" or column.name == "Male" or column.name == "MALE":
            self.maleColumn = column
          elif  column.name == "female" or column.name == "Female" or column.name == "FEMALE":
            self.femaleColumn = column


    def drawHuman(self):
        female = draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                      d="M1219.6,809.2H1033h-4c0,0,6.4-1,6.6-6c0.2-5-9.4-68.6-13.4-75.4c0,0-7.2-24.3-29.5-34.3c0,0-80.1-41.7-89.1-48.4l-21.7-21.7V609c0,0,72.2,1.2,96.9-28.9c0,0-32.5-9-37.9-63.8c-5.4-54.8-1.2-3.6-1.2-3.6s33.1-183.6-74-174c0,0-93.3-63.9-142.1,44.5c0,0-9,23.5-8.4,38.6c0,0,9,152.9-41.5,156.5c0,0,33.7,40.3,95.7,31.9v14.4l-22.9,22.9c0,0-78.3,41.5-92.1,47c0,0-18.7,9.6-24.1,28.3c0,0-11.4,42.7-12.6,68.6c0,0-2.4,17.8,8.4,17.8s593.3,0,593.3,0l0.3,61.4h-640l8.7-613.1h631.3V809.2z"
                      , transform="translate(10,-800) scale(0.6 0.6)" )
        self.d.append(female)
        male = draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                      d="M533.8,809.2l-4.3-85.4c0,0-0.8-4.8-6.4-6.8c-5.6-2-146.5-95.9-146.5-95.9s-5.6-37.3-21.3-53.8l9.3-42.5c0,0,12.4,8,14.4-5.2c2-13.3,11.3-59.4,2-65.8s-6-0.8-6-0.8s20.8-44.5-6.4-107.1c0,0-12.4-17.3-31.7-14c0,0-16.8-20.5-67.4-11.6c0,0-22.1-6.4-23.3,10.4c0,0-27.3-2-46.5,54.6c0,0-9.6,31.7,18.4,74.2c0,0-21.3-3.6-14,12.8l8,53.4c0,0,4,11.3,20.8,6.4l5.6,36.1c0,0-15.3,12.4-18.8,41.4L61.6,713c0,0-24.7,11-23,96.2l491.7,0.1h5.4h52.6v61.3H-28.3V257.4h616.6v551.8L533.8,809.2z"
                           , transform="translate(0,-800) scale(0.6 0.6)")
        self.d.append(male)

    def drawStack(self):
      print()

    def drawMaleAndFemaleStack(self):
        oldstartPoint = 0
        height = 0
        startX = 0
        length = 0
        for cell, cell2, i in zip(self.firstColumn.cells, self.femaleColumn.cells,
                                  range(0, len(self.secondColumn.cells))):
            if (type(cell2.value) != str):
                if (i != 0):
                    length += 1
                    startX += oldstartPoint
                    height = self.getLength(double(cell2.value))
                    oldstartPoint = height
                    text = str(cell.value) + ": " + str(self.percentageOfValue(double(cell2.value)))[0:4] + "%"
                    self.d.append(
                        draw.Rectangle(0, startX+800, self.widthView + 50, height, fill=self.colorList[i-1], fill_opacity=0.5,
                                       stroke="white",
                                       stroke_width=2,transform="translate(400,-100) scale(0.30 0.30)" ,id= self.Index))
                    self.metaData.append(text)
                    self.Index += 1

        oldstartPoint = 0
        height = 0
        startX = 0
        length = 0
        for cell, cell2, i in zip(self.firstColumn.cells, self.maleColumn.cells,
                                  range(0, len(self.secondColumn.cells))):
            if (type(cell2.value) != str):
                if (i != 0):
                    length += 1
                    startX += oldstartPoint
                    height = self.getLength(double(cell2.value))
                    oldstartPoint = height
                    text = str(cell.value) + ": " + str(self.percentageOfValue(double(cell2.value)))[0:4] + "%"
                    self.d.append(
                        draw.Rectangle(0, startX+800, self.widthView + 50, height, fill=self.colorList[i-1], fill_opacity=0.5,
                                       stroke="white",
                                       stroke_width=2,transform="translate(0,-100) scale(0.30 0.30)" ,id= self.Index))
                    self.metaData.append(text)
                    self.Index += 1

    def drawText(self):
      oldstartPoint = 0
      startX = 0
      length = 0
      if self.secondColumn.columnType == enums.ColumnDataType.Measures.value:
        for cell, cell2, i in zip(self.firstColumn.cells, self.secondColumn.cells,
                                  range(0, len(self.firstColumn.cells))):
          if (type(cell2.value) != str):
            if (i != 0):
              length += 1
              startX += oldstartPoint
              height = self.getLength(double(cell2.value))
              oldstartPoint = height
              text = str(cell.value)
              self.d.append(
                draw.Circle(self.widthView - 230, length * 80 + 50, 20, fill=self.colorList[i - 1], fill_opacity=0.5,
                            stroke_width=0))
              self.d.append(
                draw.Text(text=str(text), fontSize=30, x=self.widthView - 200, y=length * 80 + 50, id=self.Index))
              self.metaData.append(text)
              self.Index += 1
