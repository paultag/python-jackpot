import json

import shutil
import os
import os.path

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('jackpot')


class NoMetadataFound(Exception):
    pass


def find_metadata(module):
    """
    """
    for name, obj in module.__dict__.items():
        if name.startswith("_") or obj is Metadata:
            continue
        try:
            if issubclass(obj, Metadata):
                return obj
        except TypeError:
            continue
    raise NoMetadataFound()


class Metadata(object):
    name = None
    extractor = None

    def __init__(self):
        if self.name is None:
            raise NotImplementedError("self.name is None")

    def _save(self, obj):
        type, id = obj._id.split("/", 1)
        log.info("Saving {} {}".format(type, obj._id))

        obj.validate()

        with open(os.path.join("data", type, id), 'w') as fd:
            json.dump(obj.to_dict(), fd)

    def do_extract(self, *args):
        log.debug("starting extract {}".format(args))
        if os.path.exists("data"):
            log.debug("removing old data directory")
            shutil.rmtree("data")

        for obj in self.extract(*args):
            self._save(obj)
        log.debug("extract complete")

    def extract(self, *args):
        h = self.extractor()
        for obj in h.extract(*args):
            for other in obj._related:
                yield other
            yield obj

    def __repr__(self):
        return "<Metadata: {}>".format(self.name)


class Extractor(object):
    def extract(self, *args):
        raise NotImplementedError()
