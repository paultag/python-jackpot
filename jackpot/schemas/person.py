from .common import (other_names, identifiers)


schema = {
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "other_names": other_names,
        "identifiers": identifiers,
    },
    "type": "object",
}
