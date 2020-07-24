import drawSvg as draw
from numpy import double, os

from xml.dom import minidom
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class MapChartByLatitudeAndLongitude():
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str):
        self.animation = animation
        self.metaData = list()
        self.Index =0
        self.listOfPercentageValue =dict()
        self.widthView = 1000
        self.heightView = 1000
        self.dataSourceTableWithoutXcolumn = dataSource
        self.xColumn = XColumn
        self.idOfKeyColumn = 0
        self.zeroX = 655.3
        self.zeroY = 417.1
        self.color = self.dataSourceTableWithoutXcolumn.columnsColors[0]
        self.latColumn = self.findLatColumn()
        self.lngColumn = self.findLngColumn()
        if self.latColumn != self.xColumn and self.lngColumn != self.xColumn :
          self.listOfLength = list()
          self.d = draw.Drawing(self.widthView , self.heightView)
          self.drawlayOut()
          self.drawMap()
          self.drawPoint()
        else:
          self.d.append(draw.Text(text="Error: you have to select keyCountries in columns", fontSize=60, x=50, y=self.heightView / 2))

        self.d.setPixelScale(min(width,height)/1000)  # Set number of pixels per geometry unit
        #self.d.saveSvg(nameFile+'.svg')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView , self.heightView, fill='#ffffff'))

    def drawMap(self):
      ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
      doc = minidom.parse(str(ROOT_DIR)+"/MAP.svg")
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
        self.d.append(draw.Path(stroke_width=0.5, stroke="white", fill="green",
                                fill_opacity=0.3, d=path
                                , transform="translate(-1,-950) scale(0.75 0.75)"))
        self.Index += 1
      # self.d.append(draw.Circle(655.3,417.1, 5, fill="black", stroke_width=0, stroke='black', transform="translate(-163.3,-120.8) "))
      # self.d.append(draw.Circle(655.3,517.0, 5, fill="black", stroke_width=0, stroke='black', transform="translate(-163.3,-120.8) "))
      # self.d.append(draw.Circle(735,417.1, 5, fill="black", stroke_width=0, stroke='black', transform="translate(-163.3,-120.8) "))
      # self.d.append(draw.Circle(735,517, 5, fill="black", stroke_width=0, stroke='black', transform="translate(-163.3,-120.8) "))


    def findLatColumn(self)->ColumnModel:
      ID =0
      for column in self.dataSourceTableWithoutXcolumn.columns:
        if column.name.lower() == "lat" :
          self.dataSourceTableWithoutXcolumn.columns.pop(ID)
          self.idOfKeyColumn = ID
          self.color =  self.dataSourceTableWithoutXcolumn.columnsColors[ID]
          print(ID , "some ::", column.name)
          return column
        ID += 1

    def findLngColumn(self)->ColumnModel:
      ID =0
      for column in self.dataSourceTableWithoutXcolumn.columns:
        if column.name.lower() == "lng" :
          self.dataSourceTableWithoutXcolumn.columns.pop(ID)
          self.idOfKeyColumn = ID
          self.color =  self.dataSourceTableWithoutXcolumn.columnsColors[ID]
          print(ID , "some ::", column.name)
          return column
        ID += 1

    def convertX(self, x)->double:
      return double((x*79.7)/30)

    def convertY(self,y) -> double:
      return double((y*99.9)/30)
    def drawPoint(self):
      print("lng column:",self.lngColumn.name)
      print("lat column:",self.latColumn.name)
      i =1
      for x,y,data in zip(self.lngColumn.cells[1:],self.latColumn.cells[1:],self.xColumn.cells[1:]):
        text = self.xColumn.name + ":" + str(data.value)
        for column in self.dataSourceTableWithoutXcolumn.columns:
          text += '  '+'<br/>' +column.name + ":" + str(column.cells[i].value)
        self.d.append(draw.Circle(self.convertX(x.value)+self.zeroX,self.convertY(y.value)+self.zeroY, 1.5, fill="gray", stroke_width=0, stroke='gray',Class=self.Index,fill_opacity=1, transform="translate(-163.3,-120.8) "))
        self.metaData.append(text)
        self.Index +=1
        i += 1



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

