import drawSvg as draw

from numpy import double
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class FemaleInfChart(InfChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, animation: bool, nameFile: str):
      super().__init__(dataSource, XColumn,width, height, animation, nameFile)


    def drawHuman(self):
        p = draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                      d="M1300,990H965.2H958c0,0,11.5-1.7,11.9-10.7c0.4-9-16.9-123.1-24.1-135.4c0,0-13-43.6-52.9-61.6c0,0-143.6-74.9-159.8-86.8l-38.9-38.9v-25.9c0,0,129.6,2.2,173.9-51.8c0,0-58.3-16.2-68-114.5c-9.7-98.3-2.2-6.5-2.2-6.5s59.4-329.4-132.8-312.1c0,0-167.4-114.7-254.9,79.8c0,0-16.2,42.2-15.1,69.2c0,0,16.2,274.3-74.5,280.8c0,0,60.5,72.4,171.7,57.2v25.9l-41,41c0,0-140.4,74.5-165.2,84.2c0,0-33.5,17.3-43.2,50.8c0,0-20.5,76.7-22.7,123.1c0,0-4.3,31.9,15.1,31.9s1064.4,0,1064.4,0l0.5,110.1H0V0h1300V990z"
                      , transform="translate(0,-800) scale(0.6 0.6)" )
        self.d.append(p)

