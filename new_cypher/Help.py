import os

clear = lambda: os.system('cls')
clear()

def divider():
    print("-" * len("Multi Decoder")+ "\n")

print(f"Multi Decoder\n")
print("Created by: Ebomb\n")
print("Description: I thought this would be a fun project to have an encoding and decoding platform with minimal user input.")
divider()

print(" " * int(len("enc: Encodes/encrypts the messeage") / 2) + "Encoding / Decoding\n")

print("enc: Encodes/encrypts the messeage\n")
print("dec: Decodes/Decrypts the message\n")

divider()

print(" " * int(len("-o: Declares an output file\n") / 2) + "Files\n")
print("-f: Declares an input file\n")
print("-o: Declares an output file\n")

divider()

print(" " * int(len("-cc #: When encoding using -cc, \"#\" = shift amount\n") / 2) + "Ciphers and Dashes\n")

print("-sha1: Runs the message through sha1\n")
print("-cc: Runs message through the ceaser cipher\n")
print("-cc #: When encoding using -cc, \"#\" = shift amount\n")

divider()
