import base64


def hash(key, password):
    hash = []
    for i in range(len(password)):
        hashkey = key[i % len(key)]
        hash.append(chr((ord(password[i])+ord(hashkey)) % 256))
    return base64.b64encode("".join(hash).encode())
