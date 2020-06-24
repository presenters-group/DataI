from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.VisualizationModel import VisualizationModel


class VisualizationsController():
  @classmethod
  def insertNewVisualizer(self, data: DataModel, visio: VisualizationModel):
    id = DataController.getMaxIdInList(data.visualizations)
    visio.id = id + 1
    data.visualizations.append(visio)

  @classmethod
  def deleteVisualizer(cls,data:DataModel,id:int):
    visualizationIndex =  DataController.getElementById(data.visualizations,id)
    print(visualizationIndex)
    if visualizationIndex != -1:
      data.visualizations[visualizationIndex].isDeleted = True
      return data.visualizations[visualizationIndex]
    return None


