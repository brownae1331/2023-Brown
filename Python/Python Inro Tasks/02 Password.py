password = ""
print("Enter your password: ")
password = input()
if len(password) > 6:
    print("Password is valid")
elif len(password) <= 6:
    print("Password isn't valid")