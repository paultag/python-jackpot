import sys
import importlib

from jackpot.extract import find_metadata


def main(module, *args):
    meta = find_metadata(importlib.import_module(module))()
    report = meta.do_extract(*args)
    print(report)


if __name__ == "__main__":
    main(*sys.argv[1:])
