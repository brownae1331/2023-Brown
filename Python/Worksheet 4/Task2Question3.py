def getPword(password):
    if len(password) >= 6 and len(password) <= 8:
        attempt = 2
    else:
        attempt = 1
        print("Error. Password must be 6 to 8 characters long")
    return attempt
    
# ------------ Main Program ------------
Pword = input("enter password:")
attempt = getPword(Pword)
while attempt == 1:
    Pword = input("Error. enter password")
    attempt = getPword(Pword)
print("password accepted")
