'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false'''

class Solution:
    def wordBreak(s, wordDict):
        if not wordDict: return False
        intervals = []

        for w in wordDict:
            startIndex = 0
            while True:
                try:
                    index = s.index(w, startIndex)
                except ValueError:
                    break
                intervals.append([index, index + len(w) - 1])
                startIndex = index + 1

        intervals.sort()

        searching = {0}
        for interval in intervals:
            start, end = interval
            if start in searching:
                if end == len(s) - 1:
                    return True
                else:
                    searching.add(end + 1)

        return False

print(Solution.wordBreak("leetcode",["leet","code"]))
#True