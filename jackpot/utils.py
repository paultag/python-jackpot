

class UnsupportedMime(Exception):
    pass


def extract(path):
    import textract
    import magic

    supported_files = {
        "application/pdf": "pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    }

    mime = magic.from_file(path, mime=True)
    extension = supported_files.get(mime)
    if extension is None:
        raise UnsupportedMime(mime)

    return textract.parsers.process(path, extension=extension)
