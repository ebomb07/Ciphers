import hashlib
import os
import json

clear = lambda: os.system('cls')
clear()

result = ""
def encode(result):
    sha1 = hashlib.sha1()
    with open("config.json", "r") as f:
        config = json.load(f)
        with open(config['file'], "rb") as file:
            while True:
                info = file.read()

                if not info:
                    break

                sha1.update(info)

    result = sha1.hexdigest()
    return result

def decode():
    print("SHA1 does not support decoding")


with open("config.json", "r") as f:
    config = json.load(f)
    if config['enc'] == True:
        result = encode(result)
        with open("config.json", "r") as f:
            config = json.load(f)
            with open(config['output'], "a") as op:
                op.write(result)
    else:
        decode()


