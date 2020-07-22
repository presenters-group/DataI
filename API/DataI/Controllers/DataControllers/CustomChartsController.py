from DataI.Models.DataModel import DataModel, CustomChart


class CustomChartsController():
    @classmethod
    def addNewChart(cls, data: DataModel, svg: str, chartName):
        data.customCharts.append(CustomChart(svg, chartName))