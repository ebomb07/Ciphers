import subprocess
import os


clear = lambda: os.system('cls')
active = True
while active:
    clear()


    print("Welcome what kind of cipher would you like to use?\n\n")

    x = int(input(("[1] ceaser cipher\n[2] substitution cipher\n\n---> ")))


    if x == 1:
        active = False
        clear()
        subprocess.run(['python','ceaser_cipher.py'])
    elif x == 2:
        active = False
        clear()
        subprocess.run(['python','substitution_cipher.py'])
    else:
        pass
