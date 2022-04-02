def binarySearch(array, element, start, end):
    if start > end:
        error = "Number not in list"
        return error

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binarySearch(array, element, start, mid-1)
    else:
        return binarySearch(array, element, mid+1, end)


aList = [2, 4, 6, 8, 10, 12, 14]
print(binarySearch(aList, 8, 0, len(aList)))
