'''Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.


Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
 '''


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n, m = len(S), len(T)
        # dp[i][j] represents the length of substring starting from index i in S to cover the substring of T starting from index j
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                if S[i] == T[j]:
                    if dp[i + 1][j + 1] > 0 or j + 1 == m:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    if dp[i + 1][j] > 0:
                        dp[i][j] = 1 + dp[i + 1][j]

        startIndex = n + 1
        length = n + 1
        for i in range(n):
            if length > dp[i][0] and dp[i][0] != 0:
                length = dp[i][0]
                startIndex = i

        if startIndex == n + 1:
            return ''
        return S[startIndex: startIndex + length]

print(Solution().minWindow("abcdebdde","bde"))
#bcde