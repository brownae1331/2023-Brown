num1 = int(input())
num2 = int(input())
num3 = int(input())
max = 0
mid = 0
min = 0
if num1 > num2 and num1 > num3:   #If Num 1 is the max
    max = num1
    if num2 > num3:
        mid = num2
        min = num3
    else:
        mid = num3
        min = num2
elif num2 > num1 and num2 > num3:   #If Num 2 is the max
    max = num2
    if  num1 > num3:
        mid = num1
        min = num3
    else:
        mid = num3
        min = num1 
elif num3 > num1 and num3 > num2:    #If Num 3 is the max
    max = num3
    if num1 > num2:
        mid = num1
        min = num2
    else:
        mid = num2
        min = num1
print(min, mid, max)
