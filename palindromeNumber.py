'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''

class Solution:
    def isPalindrome(x):
        x = str(x)

        if  x == x[::-1]:
            return True
        return False

print(Solution.isPalindrome(121))