import uuid


def _coerce_value(value):
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if isinstance(value, list):
        return [_coerce_value(x) for x in value]
    return value


class BaseModel(object):
    _type = None
    _schema = None
    _related = []

    def to_dict(self):
        ret = {}
        if hasattr(self, "_id"):
            ret["_id"] = self._id
        for key in self._schema['properties']:
            value = getattr(self, key)
            ret[key] = _coerce_value(value)
        return ret


class PublicObject(BaseModel):
    def __init__(self):
        super().__init__()
        self._id = "{}/{}".format(self._type, uuid.uuid4())
