import subprocess
import os


clear = lambda: os.system('cls')
active = True
while active:
    clear()
    print("Welcome what kind of cipher would you like to use?\n\n")

    x = int(input(("[1] ceaser cipher\n\n---> ")))

    if x == 1:
        clear()
        subprocess.run(['python','ceaser_cipher.py'])
        active = False
    else:
        pass
