string = input('Enter Number: ')

def isNumeric(x):
    if (x >= '0' and x <= '9') :
        return True
    return False

def atoi(string):
    if len(string) == 0:
        return 0

    res = 0
    i = 0
    sign = 1

    if string[0] == '-':
        i = i+1
        sign = -1

    for j in range(i,len(string)):
        if isNumeric(string[j]) == False :
            return 0
        res = res * 10 + ord(string[j]) - ord('0')

    print(sign*res)

atoi(string)
