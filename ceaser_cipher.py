

x = 0
n = 0
fArray = []
arr = []

letters = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]

letters += "s","t","u","v","w","x","y","z"

letters += "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"
letters += "T","U","V","W","X","Y","Z"



start = int(input("[1] Encrypt\n[2] Decrypt\n[3] Brute force\n---> "))



    



#encrypt

if start == 1:
    user_input = str(input("What is your string\n"))
    shift = str(input("What is your shift\n"))
    array = list(user_input)

    print("\n\noriginal: " + user_input+"\n")

    arrayLength = range(len(array))

    fArray = list(arr)

    print("\n\noriginal: " + user_input)



    for x in arrayLength:

        arr = letters.index(array[x])
        arr = (letters[(arr + int(shift))])
        fArray.extend(arr)
        

    print("ceaser cipher ecryption: ") 

    print(*fArray, sep = "")


#decrypt

if start == 2:
    user_input = str(input("What is your string\n"))
    shift = str(input("What is your shift\n"))

    array = list(user_input)

    print("\n\noriginal: \"" + user_input+"\"\n")

    arrayLength = range(len(array))

    fArray = list(arr)



    for x in arrayLength:

        arr = letters.index(array[x])

        arr = (letters[(arr - int(shift))])
        fArray.extend(arr)
        print(fArray)


    print("ceaser cipher ecryption: ") 
    print(*fArray, sep = "")


#Brute force

if start == 3:
    shift = 0
    user_input = str(input("What is your string\n"))

    array = list(user_input)

    print("\n\noriginal: " + user_input+"\n")

    arrayLength = range(len(array))

    fArray = list(arr)


    for x in arrayLength:

        while n <= 52:
            shift = 1
            intArr = letters.index(array[x])

            while shift <= len(letters):

                
                arr = (letters[(intArr - int(shift))])
                fArray.extend(arr)

                print("["+str(shift)+"] " + str(fArray))
                shift += 1

            n += 1
    
