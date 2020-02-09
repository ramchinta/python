string = input('Enter String: ')
numOfChar = 256
def getCharCount(string):
    count = [0] * numOfChar
    for i in string:
        count[ord(i)] = count[ord(i)] + 1

    for i in string:
        if count[ord(i)] == 1:
            print('The first non repeated character is '+i)
            return
    print('All the characters in the string are repeated')

getCharCount(string)