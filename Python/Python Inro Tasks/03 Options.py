print("pick a number number between 1-3")
num = int(input())
while num < 1 or num > 3:
    num = int(input())
print("You have selected option number ", num)
