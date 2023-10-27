import subprocess
import os
clear = lambda: os.system('cls')
clear()

active = True

user_input = input("What is your string\n")

while active:
    clear()
    print("Current string: "+user_input)
    repString = str(input("\n\nWhat letter are you replacing?: "))
    repLetter = str(input("What string do you want to replace?: "))
    user_input = user_input.replace(repString, repLetter)
    
    if repString == 'done' and repLetter == 'done':
        active = False
        clear()
        print("your string is: \""+user_input+"\"\n\n\n")
        
    else:
        pass