from typing import List


class BasicInfo(object):
    def __init__(self, name: str, id: int, isDeleted: bool):
        self.name = name
        self.id = id
        self.isDeleted = isDeleted

    def __str__(self):
        return 'name: {}, id: {}'.format(self.name, self.id)

class BasicDataModelInfo(BasicInfo):
    def __init__(self, name: str, id: int, filter: List, isDeleted: bool):
        super().__init__(name, id, isDeleted)
        self.filters = filter

