# main.py
import sys
import json
import os
import time


clear = lambda: os.system('cls')
clear()

def uploadPayload():
    with open('config.json', 'r') as f:
        config = json.load(f)
    argv = sys.argv[1:]  # Skip the script name
    active = True
    for i in range(len(argv)):
        while active:
            arg = argv[i].casefold()
            if arg != "-h":
                match arg:
                    case "enc":
                        config['enc'] = True
                    case "dec":
                        config['enc'] = False
                    case "-cc":
                        config['payload'].append("-cc")
                        try:
                            if isinstance(int(argv[i + 1]), int) == True:
                                print("Hello")
                                config['shift'] = int(argv[i + 1])
                        except ValueError:
                            config['shift'] = -1
                    case "-o":
                        config['output'] = argv[i+1]
                    case "-f":
                        config['file'] = argv[i+1]
                    case _ if arg != config['file'] and arg != config['output'] and int(arg) != int(config['shift']):
                        config['payload'].append(arg)
            else:
                os.system("python Help.py")
                active = False

    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

    runFile()

def runFile():
    with open('config.json', 'r') as f:
        config = json.load(f)
    list = ["-sha1", "-cc"]
    for i in range(len(config['payload'])):
        for x in range(len(list)):
            if config['payload'][i] == list[x]:

                match config['payload'][i]:
                    case "-sha1":
                        #sha1
                        os.system("python files/hash/sha1.py")
                    case "-cc":
                        os.system("python files/cipher/ceaser_cipher.py")
                    case _:
                        os.system('python Help.py')



def resetConfig():

    #Has to update if items are added to config.json
    
    initial_config = {
    "file": "",
    "output": "",
    "payload": [],
    "enc": False,
    "shift": -1
}

    with open('config.json', 'w') as f:
        json.dump(initial_config, f, indent=4)


if __name__ == "__main__":
    try:
        uploadPayload()
    finally:

        #remove sleep later
        time.sleep(2)
        resetConfig()
