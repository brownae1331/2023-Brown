message = input()
for i in range(len(message)):
    Ascii = ord(message[i])
    if Ascii == 32:
        print(chr(Ascii), end="")
    elif Ascii == 121:
        print(chr(97), end="")
    elif Ascii == 122:
        print(chr(98), end="")
    elif Ascii < 97 and Ascii > 64:
        print(chr(Ascii + 34), end="")
    else: 
        print(chr(Ascii + 2), end="")
