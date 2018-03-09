from .base import PublicObject
from ..schemas.location import location


class Location(PublicObject):
    _type = "location"
    _schema = location

    def __init__(self, *, name, type):
        super().__init__()
        self.name = name
        self.type = type
