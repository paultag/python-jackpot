from .base import PublicObject
from ..schemas.relation import relation


class Relation(PublicObject):
    _type = "relation"
    _schema = relation

    def __init__(self, *, subject_person_id, type, other_person_id):
        super().__init__()
        self.subject_person_id = subject_person_id
        self.type = type
        self.other_person_id = other_person_id
