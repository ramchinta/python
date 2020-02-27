'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix( strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        cp = ""
        l = [len(st) for st in strs]
        for i in range(min(l)):
            tmp = [s[i] for s in strs]
            if min(tmp) == max(tmp):
                cp =cp +tmp[0]
            else:
                return cp
        return cp

print(Solution.longestCommonPrefix(["flower","flow","flight"]))
#fl
