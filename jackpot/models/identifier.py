from .base import BaseModel
from ..schemas.common import identifier


class Identifier(BaseModel):
    _type = "identifier"
    _schema = identifier

    def __init__(self, *, scheme, identifier):
        super().__init__()
        self.scheme = scheme
        self.identifier = identifier


class IdentifiersMixin(object):
    def add_identifier(self, *, scheme, identifier):
        id = Identifier(scheme=scheme, identifier=identifier)
        self.identifiers.append(id)
        return id
