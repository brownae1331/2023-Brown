print("Enter the time with colones between the hours, minuets and seconds")
time = input()
hours = time.split(":")[0]
minuets = time.split(":")[1]
seconds = time.split(":")[2]
print((int(hours) * 60 * 60) + (int(minuets) * 60) + int(seconds))
