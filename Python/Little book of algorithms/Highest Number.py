num1 = int(input())
num2 = int(input())
num3 = int(input())

a1 = min(num1, num2, num3)
a3 = max(num1, num2, num3)
a2 = (num1 + num2 + num3) - a1 - a3
print(a1, a2, a3)
