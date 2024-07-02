import json
import os
import time 


clear = lambda: os.system('cls')

letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



with open("config.json", "r") as f:
    config = json.load(f)

if config['enc'] == True:

    shift = config['shift']
    if shift == -1:
        print("ENCODING ERROR: add a valid integer after -cc")
    else:
        letterIndex = []
        fArray = []

        with open(config['file'], "r") as file:
            info = file.readline()
            info = info.lower()

        for i in range(len(info)):
            letterIndex.append(letters.index(info[i]))
        i = 0
        for x in range(len(letterIndex)):
            if letterIndex[x] != 0:

                if letterIndex[i] + shift > 26:
                    fArray.append(letters[abs(26 - (letterIndex[i] + shift))])
                elif (i + shift) > len(letterIndex):
                    fArray.append(letters[abs(len(letterIndex) - (i + shift))])
                else:
                    fArray.append(letters[letterIndex[i] + shift])
                i += 1

            else:
                fArray.append(letters[letterIndex[x]])
                i += 1

        with open(config['output'], "w") as out:
            out.truncate(0)
            time.sleep(1)
            for i in range(len(fArray)):
                out.write(fArray[i])

else:
    output = [[]]
    letterIndex = []

    with open(config['file'], "r") as file:
        info = file.readline()
        info = info.lower()

    for i in range(len(info)):
        letterIndex.append(letters.index(info[i]))

    output = []
    for j in range(26):
        word = ""
        for i in range(len(info)):
            if letterIndex[i] == j:
                word += letters[(letterIndex[i] - (j + 1))]
            
            if letterIndex[i] != 0:
                word += letters[(letterIndex[i] - j)]
            else:
                word += letters[letterIndex[i]]
        output.append(word)

    output.pop(0)
    with open(config['output'], "w") as out:
        out.truncate(0)
        time.sleep(1)
        out.write(f"Original: {info}\n\n######\n\nShifts:\n\n")
        for i in range(len(output)):
            out.write(f"{i + 1}: {output[i]}\n\n")
        out.write(f"26: {info}")
