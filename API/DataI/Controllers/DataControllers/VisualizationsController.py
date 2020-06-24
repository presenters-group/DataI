from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.VisualizationModel import VisualizationModel


class VisualizationsController():
  @classmethod
  def insertNewVisualizer(self, data: DataModel, visio: VisualizationModel):
    id = DataController.getMaxIdInList(data.visualizations)
    visio.id = id + 1
    data.visualizations.append(visio)



