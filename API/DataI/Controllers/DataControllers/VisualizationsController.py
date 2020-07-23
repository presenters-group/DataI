from typing import List, Dict

from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.Filters.FiltersController import FiltersController
from DataI.Models.DataModel import DataModel
from DataI.Models.TableModel import TableModel
from DataI.Models.VisualizationModel import VisualizationModel


class VisualizationsController():
    @classmethod
    def insertNewVisualizer(cls, data: DataModel, visio: VisualizationModel):
        id = DataController.getMaxIdInList(data.visualizations)
        visio.id = id + 1
        data.visualizations.append(visio)

    @classmethod
    def updateVisualizerById(cls, data: DataModel, visio: VisualizationModel, id: int):
        oldVisioIndex = DataController.getElementIndexById(data.visualizations, id)
        data.visualizations[oldVisioIndex] = visio
        return data.visualizations[oldVisioIndex]

    @classmethod
    def deleteVisualizer(cls, data: DataModel, id: int):
        visualizationIndex = DataController.getElementById(data.visualizations, id)
        print(visualizationIndex)
        if visualizationIndex != -1:
            data.visualizations[visualizationIndex].isDeleted = True
            return data.visualizations[visualizationIndex]
        return None

    @classmethod
    def getFilteredTable(cls, data: DataModel, signatureMatcher: int, visioId: int) -> TableModel:
        return FiltersController.getFilteredVisioTable(data, visioId)
