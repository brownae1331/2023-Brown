max = 0
min = 10000
mid = 0
for i in range(3):
    print("Enter number :")
    number = int(input())
    if number > max:
        max = number
    elif number < min:
        min = number 
    else:
        mid = number
print(min, mid, max)
