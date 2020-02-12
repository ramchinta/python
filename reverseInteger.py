'''Given a 32-bit signed integer, reverse digits of an integer.'''
'''Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.'''

class Solution:
    def reverse(x):
        if x>0 :
            a =  int(str(x)[::-1])
        if x<=0:
            a = -1*int(str(-1*x)[::-1])
        if a not in range(-2**31,2**31-1):
            return 0
        else:
            return a
print(Solution.reverse(-9584))