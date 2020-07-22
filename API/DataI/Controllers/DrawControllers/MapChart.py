import drawSvg as draw
from numpy import double, os

from xml.dom import minidom

from DataI import enums
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class MapChart():
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str):
        self.animation = animation
        self.metaData = list()
        self.Index =0
        self.listOfPercentageValue =dict()
        self.widthView = 1000
        self.heightView = 1000 - 1000/3
        self.dataSourceTableWithoutXcolumn = dataSource
        self.xColumn = XColumn
        # print(XColumn.name)
        self.keyColumn = self.findKeyColumn()
        if self.keyColumn != self.xColumn:
          self.listOfLength = list()
          self.d = draw.Drawing(self.widthView , self.heightView)
          self.total = self.sumColumn(self.xColumn)
          self.drawlayOut()
          self.drawMap()
        else:
          self.d.append(draw.Text(text="Error: you have to select keyCountries in columns", fontSize=60, x=50, y=self.heightView / 2))

        self.d.setPixelScale(min(width,height)/1000)  # Set number of pixels per geometry unit
        # self.d.saveSvg(nameFile+'.svg')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView , self.heightView, fill='#ffffff'))

    def drawMap(self):
      ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
      doc = minidom.parse(str(ROOT_DIR)+"/M.svg")
      path_id = [path.getAttribute('id') for path
                 in doc.getElementsByTagName('path')]
      path_data = [path.getAttribute('d') for path
                   in doc.getElementsByTagName('path')]

      data_name = [path.getAttribute('data-name') for path
                   in doc.getElementsByTagName('path')]
      doc.unlink()
      i=0
      for path, id ,dataname in zip(path_data, path_id,data_name):
        i+=1
        if self.keyColumn.name.lower() == "geoid" :
          key = id
        else:
          key = dataname
        meta =  self.xColumn.name +":"+str(self.xColumn.cells[self.findIndexForCountryBykey(key)].value)
        for column in self.dataSourceTableWithoutXcolumn.columns:
          meta += '\n'+ str(column.name)+":"+str(column.cells[self.findIndexForCountryBykey(key)].value)
        self.metaData.append(meta)
        self.d.append(draw.Path(stroke_width=1, Class=self.Index, id=self.Index, stroke="white", fill="gray",
                                fill_opacity=0.2, d=path
                                , transform="translate(-80,-950) scale(1.15 1.19)"))
        self.d.append(draw.Path(stroke_width=0, Class=self.Index,id=self.Index, stroke="white", fill=self.dataSourceTableWithoutXcolumn.columnsColors[self.keyColumn.id],
                                fill_opacity=self.getPercentageOfCountryKey(str(key))/80,d=path
                                , transform="translate(-80,-950) scale(1.15 1.19)" ))
        self.Index += 1

    def findKeyColumn(self)->ColumnModel:
      for column in self.dataSourceTableWithoutXcolumn.columns:
        if column.name.lower() == "geoid" :
          self.dataSourceTableWithoutXcolumn.columns.pop(column.id)
          return column
      for column in self.dataSourceTableWithoutXcolumn.columns:
        if column.name.lower() == 'countries' :
          self.dataSourceTableWithoutXcolumn.columns.pop(column.id)
          return column
      return self.xColumn

    def getPercentageOfCountryKey(self,key:str)->double:
      if (self.findIndexForCountryBykey(key) == -1):
        return double(0)
      else:
        return self.percentageOfValue(double(self.xColumn.cells[self.findIndexForCountryBykey(key)].value))


    def percentageOfValue(self, value: double) -> double:
      return double((abs(value) / self.total) * 100)

    def CorrectPercentageOfValue(self, value: double) -> int:
        return int((int(abs(value)*100))/ 100)

    def findIndexForCountryBykey(self,key:str)->int:
      i=-1
      for cell in self.keyColumn.cells:
        i += 1
        if key == cell.value:
          return i
      return -1

    def sumColumn(self, column: ColumnModel) -> double:
      Max = 0
      for cell in self.xColumn.cells:
        if (cell.type == enums.CellType.numeric.value):
          if (double(cell.value) > Max):
            Max = double(cell.value)
      return Max

    def saveAsSVG (self)->str:
      current = os.path.dirname(__file__)
      filePath = current[:len(current) - 33] + 'media/download/svg/'
      self.d.saveSvg(filePath+'Chart.svg')
      return filePath+'Chart.svg'

    def saveAsPNG (self)->str:
      current = os.path.dirname(__file__)
      filePath = current[:len(current) - 33] + 'media/download/svg/'
      self.d.saveSvg(filePath+'Chart.png')
      return filePath+'Chart.png'
