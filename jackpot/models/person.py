from .base import PublicObject
from .identifier import IdentifiersMixin
from .other_name import OtherNameMixin
from .relation import Relation

from ..schemas.person import schema


class Person(PublicObject, IdentifiersMixin, OtherNameMixin):
    _type = "person"
    _schema = schema

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.other_names = []
        self.identifiers = []

    def add_relation(self, *, type, name):
        other = Person(name=name)
        self._related.append(other)
        rel = Relation(subject_person_id=self._id, type=type, other_person_id=other._id)
        self._related.append(rel)
        return rel
