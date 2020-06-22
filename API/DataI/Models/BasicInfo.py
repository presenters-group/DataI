from typing import List


class BasicInfo(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @classmethod
    def getMaxIdInList(self, idList: List):
        max = 0
        for item in idList:
            if item.id > max:
                max = item.id
        return max

    def __str__(self):
        return 'name: {}, id: {}'.format(self.name, self.id)
