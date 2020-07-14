import random
from typing import List
import drawSvg as draw
from numpy import double

from DataI import enums
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Controllers.DrawControllers.chart import Chart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class HealthyFoodChart(InfChart):
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, nameFile: str):
        super().__init__(dataSource, XColumn,width, height, nameFile)

    def drawHuman(self):
        p = draw.Path(stroke_width=0, stroke="gray", fill="white", fill_opacity=1,
                      d="M730.8,990c0,0,81.3-44.1,116.8-126.4c0,0,100.9-218,82.3-348.5c0,0-24.1-190.5-227.1-199.9c0,0-59.4-5.5-120.9,36.3c0,0,29.7-77.9,141.7-129.8c0,0,17.3-17.3,6.5-33.6c0,0-7.1-15.1-27.2-13.8c-20,1.3-108.9,59.4-129.4,91.4c0,0-12.9-96.8-133.9-154.6c0,0-15.8-5.1-27.5,9.1c0,0-30.1,56-22.4,129.4c0,0,1.5,35.4,21.2,70.8c0,0-234.1-51.2-276,211c0,0-0.4,181.5,94,350c0,0,60.7,138.9,205.4,129.5c0,0,68.4-3.4,99-33.4c0,0,70,64.8,190.3,16l6.6-3.2H1299h1V1100H0V0h1300v990L730.8,990z"
                      , transform="translate(0,-796) scale(0.6 0.55)" )
        self.d.append(p)

