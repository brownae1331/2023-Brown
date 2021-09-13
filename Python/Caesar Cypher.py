message = input()
cypher = ""
for i in range(len(message)):
    Ascii = ord(message[i])
    if Ascii < 97:
         cypher[i] = chr(Ascii + 34)
    elif Ascii == 121:
        cypher[i] = chr(97)
    elif Ascii == 122:
        cypher[i] = chr(98)
    elif Ascii == 32:
        cypher[i] = " "
    else: 
        cypher[i] = chr(Ascii + 2)
print(cypher)
