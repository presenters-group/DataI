import drawSvg as draw
from numpy import double
from DataI.Controllers.DrawControllers.ManInfChart import ManInfChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel

class PyramidalChart(ManInfChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str):
      super().__init__(dataSource, XColumn, width, height, animation, nameFile)

    def drawHuman(self):
      p = draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                    d="M920.8,982.5L549.9,134.1c0,0-14.5-20.8-33,0l-373,854c0,0-8,24.4,24.4,24.4s739.1,0,739.1,0s23.4-4.9,14.3-28.7L920.8,982.5l379.2,0V1100H0V0h1300v982.5l-379.2,0.1L920.8,982.5z"
                    , transform="translate(0,-800) scale(0.6 0.6)")
      self.d.append(p)
