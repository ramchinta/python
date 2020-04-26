list = ['a','b','c','a','d','e','b','a','c']
result = []
for i in list:
    if i not in result:
        result.append(i)
print(result)


list = [3, 8, 20, 32, 27, 49, 12, 9, 2, 4, 11, 14, 12] #  -->   [(27, 20), (9, 2), (11, 4)]

def findPair(list, n):
    list.sort()
    size = len(list)

    # Initialize positions of two elements
    i, j = 0, 1
    result = []
    # Search for a pair
    while i < size and j < size:

        if i != j and list[j] - list[i] == n:
            res = (list[j], list[i])
            result.append(res)
            i = i + 1
            j = j + 1

        elif list[j] - list[i] < n:
            j += 1
        else:
            i += 1
    return result
print(findPair(list, 7))

