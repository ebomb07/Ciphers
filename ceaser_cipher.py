fArray = []
arr = []
finalArray = []


letters = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]

letters += "s","t","u","v","w","x","y","z"




start = int(input("[1] Encrypt\n[2] Decrypt\n[3] Brute force\n---> "))

def string_maker(a_list):
    ret_string = ""
    for val in a_list:
        ret_string = ret_string + val
    return ret_string

#encrypt

if start == 1:
    user_input = str(input("What is your string\n")).lower()
    shift = str(input("What is your shift\n"))
    array = list(user_input)

    print("\n\noriginal: " + user_input+"\n")

    arrayLength = range(len(array))

    fArray = list(arr)



    for x in arrayLength:

        arr = letters.index(array[x])
        arr = (letters[(arr + int(shift))])
        fArray.extend(arr)
        

    print("ceaser cipher ecryption: \"" +str(string_maker(fArray))+"\"\n") 


#decrypt

if start == 2:
    user_input = str(input("What is your string\n")).lower()
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


    print("\nceaser cipher decryption: \"" +str(string_maker(fArray))+"\"\n")  


#Brute force

if start == 3:
    user_input = str(input("What is your string\n")).lower()

    array = list(user_input)

    print("\n\noriginal: \"" + user_input+"\"\n")
    fArray = list(arr)
    arrayLength = range(len(array))
    cipherList = {}
            
    shift = 0
    i = 0

    for x in arrayLength:
        intArr = letters.index(array[x])
        fArray.append(intArr)


    fArrayLen = range(len(fArray))
    for j in range(26):
        temp = []
        for i in  fArrayLen:
        
            array = letters[fArray[i] - int(j)]
            temp.append(array)
        cipherList[j] = temp

    for key, value in cipherList.items():
        print(str(key) +": "+ str(string_maker(value)) +"\n")
        