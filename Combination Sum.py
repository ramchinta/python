'''Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(candidates) == 0:
            return []

        self.dp, self.minCand, self.candidates = {}, min(candidates), set(candidates)

        return self.dfs(target)

    def dfs(self, target):
        if target < self.minCand:
            return None
        elif target in self.dp:
            return self.dp[target]

        for i in self.candidates:
            if i > target - i:  # optimization
                continue
            childR = self.dfs(target - i)  # compute child
            if childR:
                if not target in self.dp:
                    self.dp[target] = []
                for k in childR:
                    if i > k[0]:  # to avoid duplicate
                        continue
                    self.dp[target].append([i] + k)

        if target in self.candidates:
            if not target in self.dp:
                self.dp[target] = [[target]]
            else:
                self.dp[target].append([target])

        if target in self.dp:
            return self.dp[target]
        return None

print(Solution().combinationSum([2,3,5],8))
#[[2, 2, 2, 2], [2, 3, 3], [3, 5]]