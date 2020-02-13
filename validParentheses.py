'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.'''
class Solution:
    def isValid(s):
        bracketMap = {'(': ')', '[': ']', '{': '}'}
        openPar = set(['(', '{', '['])
        stack = []
        for i in s:
            if i in openPar:
                stack.append(i)
            elif stack and i == bracketMap[stack[-1]]:
                stack.pop()
            else:
                return False

        return stack == []

print(Solution.isValid('{()'))