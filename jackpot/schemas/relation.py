
relation = {
    "properties": {
        "subject_person_id": {"type": "string", "minLength": 1},
        "other_person_id": {"type": "string", "minLength": 1},
        "type": {"type": "string"},
    },
}

relations = {
    "items": relation,
    "type": "array",
}
