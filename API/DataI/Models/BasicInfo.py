from typing import List


class BasicInfo(object):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return 'name: {}, id: {}'.format(self.name, self.id)
