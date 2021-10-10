def multiples(f1, f2start, f2end, name):
    print("Hi", name, "here is your times table")
    for i in range(f2start, f2end + 1):
        print(f1, "x", i, "=", f1 * i)

# ---------- Main Program ----------
pupilName = input("What is your name?")
Table = int(input("Enter times table, start number and end number"))
startNum = int(input())
endNum = int(input())
multiples(Table, startNum, endNum, pupilName)
