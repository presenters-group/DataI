from DataI.Controllers.DataControllers import DataController
from DataI.Models.DataModel import DataModel
from DataI.Models.FilterModel import FilterModel


class FiltersController():
  @classmethod
  def inserNewFilter(cls, data: DataModel, filter: FilterModel):
    id = DataController.getMaxIdInList(data.filters)
    filter.id = id + 1
    data.filters.append(filter)

  @classmethod
  def deleteFilter(cls,data:DataModel, id:int):
      filterIndex = DataController.getElementById(data.filters,id)
      if filterIndex != -1:
        data.filters[filterIndex].isDeleted = True
        return data.filters[filterIndex]
      return None

  @classmethod
  def updateFilterById(cls, data: DataModel, filter: FilterModel, id: int):
    oldFilterIndex = DataController.getElementIndexById(data.filters, id)
    data.filters[oldFilterIndex] = filter
    return data.filters[oldFilterIndex]
