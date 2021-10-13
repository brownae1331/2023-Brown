park = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

ID = input("Enter the registration number:")

while True:
    row = int(input("Enter row number:"))
    col = int(input("Enter col number:"))
    if row >= 1 and row <= 10 and col >= 1 and col <= 5:
        break

park[row][col] = ID

for i in range(10):
    for ii in range(5):
        print(park[i][ii], end=" ")
