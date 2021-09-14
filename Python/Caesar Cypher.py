message = input()
for i in range(len(message)):  
    Ascii = ord(message[i])   #Turning each letter of the sentece into Ascii
    if Ascii == 32:           #If the charater is a space
        print(chr(Ascii), end="")
    elif Ascii == 121:        #If the charater is 'y' 
        print(chr(97), end="")
    elif Ascii == 122:        #If the charater if 'x'
        print(chr(98), end="")
    elif Ascii < 97 and Ascii > 64: #If the character is a capital
        print(chr(Ascii + 34), end="") 
    else: 
        print(chr(Ascii + 2), end="")
