'''Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the
behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.'''

class Solution:
    def isNumeric(self, x):
        if (x >= '0' and x <= '9'):
            return True
        return False

    def myAtoi(self, str):

        for i in str:
            if i == ' ':
                str = str[str.index(i) + 1:]
            else:
                break

        sign = 1

        if len(str) == 0 or str == '-' or str == '+':
            return 0

        str1 = ''

        if self.isNumeric(str[0]) == True:
            str1 = str1 + str[0]
        elif str[0] == '-':
            sign = -1
        elif str[0] == '+':
            sign = 1
        else:
            return 0

        for j in str[1:]:
            if self.isNumeric(j) == True:
                str1 = str1 + j
            else:
                break

        if self.isNumeric(str1[1:]) != True:
            return 0
        else:
            a = sign * int(str1)

        if a > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif a < -2 ** 31:
            return -2 ** 31
        else:
            return a




print(Solution.myAtoi('-52'))