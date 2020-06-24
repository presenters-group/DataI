from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel


class FiltersController():
  @classmethod
  def inserNewFilter(cls, data: DataModel, filter: FilterModel):
    id = DataController.getMaxIdInList(data.filters)
    filter.id = id + 1
    data.filters.append(filter)
