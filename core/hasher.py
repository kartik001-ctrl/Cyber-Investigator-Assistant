import hashlib

def sha256_text(data):
    return hashlib.sha256(data.encode()).hexdigest()
