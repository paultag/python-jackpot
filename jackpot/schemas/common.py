identifier = {
    "properties": {
        "identifier": {"type": "string", "minLength": 1},
        "scheme": {"type": "string"},
    },
}

identifiers = {
    "items": identifier,
    "type": "array",
}

other_name = {
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "note": {"type": "string"},
    },
    "type": "object",
}

other_names = {
    "items": other_name,
    "type": "array",
}
