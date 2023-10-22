import subprocess
import os


clear = lambda: os.system('cls')

clear()
print("Welcome what kind of cipher would you like to use?\n\n")

x = int(input(("[1] ceaser cipher\n\n---> ")))

if x == 1:
    clear()
    subprocess.run(['python','ceaser_cipher.py'])


if x == 2:
    for i in range(5):
        print(i, end=" ")
        print()