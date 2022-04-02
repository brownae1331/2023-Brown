def linearSearch(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i


array = [1, 5, 3, 2, 7, 5, 8]
print(linearSearch(array, 7))
