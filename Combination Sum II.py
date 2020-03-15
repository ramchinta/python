'''Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]'''

class Solution(object):
    def backtrack(self, dic, k, track, trackSum, target):
        """
        :type dic: dict[int:int]
        :type k: int
        :type track: List[int]
        :type trackSum: int
        :type target: int
        """
        if target == trackSum:
            self.res.append(track[:])
            return
        i = 0
        for key, val in dic.items():
            if i < k or val <= 0 or trackSum + key > target:
                i += 1
                continue
            track.append(key)
            trackSum += key
            dic[key] -= 1
            if dic[key] == 0:
                self.backtrack(dic, i+1, track, trackSum, target)
            else:
                self.backtrack(dic, i, track, trackSum, target)
            track.pop()
            trackSum -= key
            dic[key] += 1
            i += 1

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        if len(candidates) == 0:
            return self.res
        dic = {}
        for num in candidates:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        track, trackSum = [], 0
        self.backtrack(dic, 0, track, trackSum, target)
        return self.res

print(Solution().combinationSum2 ([10,1,2,7,6,1,5],8))
#[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]