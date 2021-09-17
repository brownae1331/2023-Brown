print("Write a number between 100 and 999")
number = int(input())
print(number // 100, "hundreds", (number // 10) % 10, "tens", number % 10, "units")