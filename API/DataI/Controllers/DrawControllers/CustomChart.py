from xml.dom import minidom

import drawSvg as draw

from numpy import double
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class CustomChart(InfChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str,dir:str):
      self.dir = dir
      super().__init__(dataSource, XColumn,width, height, animation, nameFile)

    def drawHuman(self):
      doc = minidom.parse(self.dir)
      path_data = [path.getAttribute('d') for path
                   in doc.getElementsByTagName('path')]
      doc.unlink()
      for path in path_data:
        print(path)
        self.d.append(draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                      d=str(path), transform="translate(0,-800) scale(0.6 0.6)" ))


