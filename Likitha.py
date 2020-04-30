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

#Sample question asked
from itertools import combinations
dict = {75:250,45:280,35:120,30:200,15:100,60:300,90:350,20:110,10:90}
dict2 = {'PacMan': 250,'speed racer':280,'pump it up':120,'space invaders':200,'mortal kombat':100,'Atari Breakout':300,'Super tetris':350,'Star wars':110,'Street fighter II':90}
numbers = (dict.keys())

result = [seq for i in range(len(numbers), 0, -1) for seq in combinations(numbers, i) if sum(seq) <= 120]
result2 = []
for i in result:
    temp = []
    for j in list(i):
        temp.append(dict[j])
    result2.append(temp)


maximumSumList = (max(result2,key=sum))
def get_key(val):
    for key, value in dict2.items():
         if val == value:
             return key
for i in maximumSumList:
    print(get_key(i))

