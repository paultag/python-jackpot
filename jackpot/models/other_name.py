from .base import BaseModel
from ..schemas.common import other_name


class OtherName(BaseModel):
    _type = "other_name"
    _schema = other_name

    def __init__(self, *, name, note=""):
        super().__init__()
        self.name = name
        self.note = note


class OtherNameMixin(object):
    def add_other_name(self, *, name, note=""):
        name = OtherName(name=name, note=note)
        self.other_names.append(name)
        return name
