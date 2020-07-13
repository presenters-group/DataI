from typing import List, Dict

from DataI.Controllers.DataControllers import DataController
from DataI.Controllers.Filters.FilterController import FiltersController
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
    def getFinalTable(cls, data: DataModel, visioId: int) -> TableModel:
        # Aggregation should be added here.
        return cls.__getFilteredTable(data, visioId)

    @classmethod
    def insertInVisioFilter(cls, data: DataModel, filter: Dict, visioId: int):
        targetVisioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        data.visualizations[targetVisioIndex].filters.append(filter)
        return filter

    @classmethod
    def updateInVisioFilter(cls, data: DataModel, filter: Dict, visioId: int, filterId: int):
        targetVisioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        inFilterIndex = DataController.getElementIndexFromDictById(data.visualizations[targetVisioIndex].filters,
                                                                   filterId)
        if inFilterIndex == -1:
            return -1
        data.visualizations[targetVisioIndex].filters[inFilterIndex] = filter
        return filter

    @classmethod
    def removeInVisioFilter(cls, data: DataModel, visioId: int, filterId: int):
        targetVisioIndex = DataController.getElementIndexById(data.visualizations, visioId)
        inFilterIndex = DataController.getElementIndexFromDictById(data.visualizations[targetVisioIndex].filters,
                                                                   filterId)
        if inFilterIndex == -1:
            return -1
        data.visualizations[targetVisioIndex].filters.pop(inFilterIndex)
        return 1

    @classmethod
    def __getFilteredTable(cls, data: DataModel, visioId: int) -> TableModel:
        return FiltersController.getFilteredVisioTable(data, visioId)
