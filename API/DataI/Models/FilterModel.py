from DataI.JSONSerializer import ObjectDeserializer
from DataI.Models.BasicInfo import BasicInfo


class FilterModel(ObjectDeserializer, BasicInfo):
    def __init__(self, name: str, id: int, dataSource: int, filteredColumn: int, initValue: object,
                 type: str, isDeleted: bool):
        super(FilterModel, self).__init__(name, id)
        self.dataSource = dataSource
        self.filteredColumn = filteredColumn
        self.initValue = initValue
        self.type = type
        self.isDeleted = isDeleted

    def __str__(self):
        return 'name: {}, ID: {}, dataSourceTableWithoutXcolumn source: {},' \
               ' filtered column: {}, initial value: {}, filter type: {}, isDeleted: {}\n'\
            .format(self.name, self.id, self.dataSource, self.filteredColumn, self.initValue, self.type, self.isDeleted)

