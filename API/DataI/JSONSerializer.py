from json import JSONEncoder


class ObjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class ObjectDeserializer():
    @classmethod
    def from_json(cls, data):
        return cls(**data)
