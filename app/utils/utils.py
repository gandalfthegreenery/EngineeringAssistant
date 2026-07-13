import hashlib


def compute_file_hash(path:str)->str:
    hasher=hashlib.sha256()

    with open(path,"rb") as file:
        for block in iter(lambda:file.read(4096),b""):
            hasher.update(block)

    return hasher.hexdigest()