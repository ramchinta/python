'''3. Longest Substring Without Repeating Characters'''

class Solution:
    def lengthOfLongestSubstring(s):
        a = ''
        l = 0
        for i in s:
            if i in a:
                if len(a) > l:
                    l = len(a)
                '''If the character repeats removes the character in the first position a[0]'''
                a = a[a.index(i)+1:]
            a = a+i
        if len(a)>l:
            l = len(a)
        return l

print(Solution.lengthOfLongestSubstring('aabbccddabcdef'))