from numpy import double, long

from Charts.chart import Chart
from DataI import enums
from DataI.Models.ColumnModel import  ColumnModel
from DataI.Models.TableModel import  TableModel
import drawSvg as draw

class PointChart (Chart):
  def __init__(self,dataSource:TableModel,width:double,height:double,Xcolomn:ColumnModel,quality:double,nameFile):
    super().__init__(dataSource, width,height)
    self.lsitOfIndexing = list()
    self.Index = 0
    self.Xcolumn = Xcolomn
    self.widthOfsidelable = 200
    self.heightOfbuttomLable =200
    self.widthView = (len(Xcolomn.cells))*150+200
    self.widthOfCoordinatePlane = self.widthView - self.widthOfsidelable
    self.heightOfCoordinatePlane = self.heightView - self.heightOfbuttomLable
    self.quality = quality
    self.d = draw.Drawing(self.widthView, self.heightView)
    self.listofLevelValue = list()
    self.drawlayOut()
    self.maximumValue = self.findMaximumValue()
    self.minimumValue = self.findMinimumValue()
    self.distant = self.getDistant()
    self.yUnit = self.getyUnit()
    self.xUnit = self.getxUnit()
    self.yStep = self.getYstep()
    self.yUnit = self.correctingUnit()
    self.getlevelsValue()
    if (len(self.listofLevelValue)!= 0):
      self.startValue = self.listofLevelValue[0]
    else:
      self.startValue = self.listofLevelValue[0]
    self.drawlayOut()
    self.drawLineLevels()
    self.drawPoints()
    self.drawXpoints(double(20))
    self.drawSideLable()
    self.d.saveSvg(nameFile+'.svg')
    self.d.savePng(nameFile+'.png')
    self.SVG = self.d.asSvg()



  def drawlayOut(self):
    self.d.append(draw.Rectangle(0, 0, self.widthView, self.heightView, fill='#ffffff'))
  def getStartvalue(self) -> double:
    num=0
    if(len(self.listofLevelValue)!=0):
      num = self.listofLevelValue[0]
      for value in self.listofLevelValue:
        if (value == 0):
         num = 0
    return num
  def findStartYvalue(self):
    for column in self.data.columns:
      if (column != self.Xcolumn):
        for i in range(1, len(column.cells)):
          if (type(column.cells[i].value) != type(str)):
            return column.cells[i].value
    return 0
  def findMinimumValue(self):
    min = self.findStartYvalue()
    for column in self.data.columns:
      if (column != self.Xcolumn):
        for cell in column.cells:
          if (cell.type == enums.CellType.numeric.value):
            if (double(cell.value) < min):
              min = cell.value
    return min
  def findMaximumValue(self):
    Max = self.findStartYvalue()
    for column in self.data.columns:
      if (column != self.Xcolumn):
        for cell in column.cells:
          if (cell.type == enums.CellType.numeric.value):
            if (double(cell.value) > Max):
              Max = cell.value
    return Max
  def getDistant(self):
    if (self.maximumValue == self.minimumValue):
      return self.maximumValue
    return self.maximumValue - self.minimumValue
  def getyUnit(self) -> double:
    return double(self.distant / (self.quality - 2))
  def getxUnit(self) -> double:
    return double(self.widthOfCoordinatePlane / (len(self.Xcolumn.cells)))
  def getYstep(self) -> double:
    return double(self.heightOfCoordinatePlane / (self.quality - 1))
  def getXPointlInSVG(self,i: int) -> double:
    return double((i * self.xUnit) + self.widthOfsidelable)
  def drawXpoints(self,fontSize:double):
    add = 200
    for cell, i in zip(self.Xcolumn.cells, range(0, len(self.Xcolumn.cells))):
      if (i != 0):
        add += 150
        num = self.Xcolumn.cells[i].value
        self.lsitOfIndexing.append(str(num))
        if (len(str(num)) > 10):
          num = num[0:8] + "..."
        widthOfText = len(str(num)) * 3 * ((fontSize / 10) * 50 / 50)
        self.d.append(draw.Circle(add, self.heightOfbuttomLable, 8,fill="black", stroke_width=0, stroke='black'))
        self.d.append(draw.Text(text=str(num), fontSize=fontSize, x=add - widthOfText, y=self.heightOfbuttomLable / 1.3, id=str(self.Index)))
        self.Index += 1
  def getLastLevel(self,min:double,unit:double) -> double:
    i = 0
    level = 0
    while(double(level)>min):
      i+=1
      level -= unit
    self.minimumValue = level
    return double(level)
  def getCloseNumber(self,num)->double:
    temp = num % 10
    num -= temp
    if (temp < 5):
      num += 5
    else:
      num += 10
    return num
  def correctingUnit(self):
    integer = long(self.yUnit)
    beforeTheComma = self.yUnit - integer
    t = long(beforeTheComma * 100)
    t = self.getCloseNumber(t) / 100
    return integer + t
  def getlevelsValue(self):
    unt = self.correctingUnit()
    if ((self.minimumValue < 0) & (self.maximumValue > 0)):
      min = self.getLastLevel(double(self.minimumValue),unt)
      for i in range(0, int(self.quality)):
        self.listofLevelValue.append(min)
        min += unt
    else:
      for i in range(0, self.quality):
        self.listofLevelValue.append(min)
        min += unt
  def findZeroInSVG(self) -> double:
    for value in self.listofLevelValue:
      if (long(value) == 0):
        return double(0)
    return self.listofLevelValue[0]
  def convertY(self,value) -> double:
    return double(((value - self.startValue) * self.yStep) / self.yUnit + self.widthOfsidelable)
  def drawLineLevels(self):
    y = self.heightOfbuttomLable
    for i in range(0, self.quality):
      p = draw.Path(stroke_width=1, stroke='gray',
                    fill='gray', fill_opacity=0.5)
      p.M(self.widthOfsidelable, self.convertY(self.listofLevelValue[i]))
      p.h(self.widthOfCoordinatePlane)
      self.d.append(p)
      y += self.yStep
  def drawPoints(self):
    for column in self.data.columns:
      add = 200
      if (column != self.Xcolumn):
        for cell, i in zip(column.cells, range(0, len(self.Xcolumn.cells))):
          if (i != 0):
            add += 150
            self.lsitOfIndexing.append("("+str(self.Xcolumn.cells[i].value)+","+str(cell.value)+")")
            self.d.append(draw.Circle(add, self.convertY(double(cell.value)), 5,fill=column.style.color, stroke_width=0, stroke='black', id= (self.Index)))
            self.Index += 1
  def drawSideLable(self):
    y = self.heightOfbuttomLable
    add = 200
    for i in range(0, self.quality):
      add += 150
      num = str(self.listofLevelValue[i])
      self.lsitOfIndexing.append(num)
      if (len(num) > 10):
        num = num[0:8] + "..."
      self.d.append(draw.Circle(self.widthOfsidelable, self.convertY(self.listofLevelValue[i]), 8,fill="lightgray", stroke_width=5, stroke='gray'))
      self.d.append(draw.Text(text=str(num), fontSize=20, x=(self.widthOfsidelable / 3.5),y=self.convertY(self.listofLevelValue[i]),id=str(self.Index)))
      self.Index += 1
