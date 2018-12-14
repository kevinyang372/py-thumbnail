from .thumbnail import thumbnail

# read and scan the document
def read_file(directory, silent = True, keys = ['class', 'def', 'for', 'if', 'elif','else:', 'while']):
    snapshot = thumbnail(directory, silent, keys)
    snapshot.scan()
    return snapshot