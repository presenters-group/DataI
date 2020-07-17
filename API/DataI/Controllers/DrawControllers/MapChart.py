import drawSvg as draw
from numpy import double

from xml.dom import minidom
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class MapChart(InfChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, nameFile: str):
      self.listOfOpacityValue =dict()
      super().__init__(dataSource, XColumn,width, height, nameFile)

    def drawHuman(self):

      doc = minidom.parse("/home/kareem/m.svg")
      path_id = [path.getAttribute('id') for path
                 in doc.getElementsByTagName('path')]
      path_data = [path.getAttribute('d') for path
                   in doc.getElementsByTagName('path')]
      doc.unlink()
      for path, id in zip(path_data, path_id):
        print("new:",id, ":", path)
        self.d.append(draw.Path(stroke_width=1,id=id, stroke="red", fill="red",
                                fill_opacity=self.listOfOpacityValue["SY"]/100,d=path
                                , transform="translate(0,-800) scale(0.8 0.8)" ))
    def drawStack(self):
      for cell in self.xColumn.cells:
        print("celllllll",cell.value)
      for cell in self.LabelColumn.cells[1:]:
        # print("lable",cell.value)
        # cell = self.LabelColumn.cells[1]
        # cell.value = "SY"
        value = self.percentageOfValue(double(self.xColumn.cells[self.LabelColumn.cells.index(cell)].value))
        self.listOfOpacityValue[cell.value] = value
        print("value "+cell.value+":",self.listOfOpacityValue["SY"])
        # oldstartPoint = 0
        # timer = 1
        # startX = 0
        # length = 0
        # for cell, cell2, i in zip(self.LabelColumn.cells, self.xColumn.cells,
        #                           range(0, len(self.xColumn.cells))):
        #     if (type(cell2.value) != str):
        #         if (i != 0):
        #             length += 1
        #             startX += oldstartPoint
        #             height = self.getLength(double(cell2.value))
        #             oldstartPoint = height
        #             text = str(cell.value) + ": " + str(self.percentageOfValue(double(cell2.value)))[0:4] + "%"
        #             t =draw.Rectangle(0, startX+800, self.widthView + 50, height, fill=self.colorList[i-1], fill_opacity=0.5,stroke="white",stroke_width=2,transform="translate(0,+200) scale(0.6 0.55)" ,id= self.Index)
        #             t.appendAnim(draw.Animate('width', str(timer)+'s', from_or_values=0, to=self.widthView + 50 ,repeatCount='1'))
        #             self.d.append(t)
        #             self.metaData.append(text)
        #             timer += 0.05
        #             self.Index += 1

    def drawText(self):
      print()
