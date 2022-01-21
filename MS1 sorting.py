def bubbleSort(array, count):
    n = len(array)

    for i in range(n):
        count += 1
        for j in range(0, n - i - 1):
            count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count += 1
    return count


def insertionSort(array, count):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        count += 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            count += 1
        array[j + 1] = key
    return count


bubble = [64, 34, 25, 12, 22, 11, 90]
insertion = [64, 34, 25, 12, 22, 11, 90]

bubbleCount = 0
insertionCount = 0

bubbleCount = bubbleSort(bubble, bubbleCount)
insertionCount = insertionSort(insertion, insertionCount)

print(bubble, " ", bubbleCount)
print(insertion, " ", insertionCount)
