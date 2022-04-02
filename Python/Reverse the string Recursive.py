def stringReverse(word):
    if len(word) == 1:
        return word[0]
    else:
        return word[len(word) - 1] + stringReverse(word[:-1])


list = ['a', 'b', 'c', 'd', 'e']
reverseList = stringReverse(list)
print(reverseList)
