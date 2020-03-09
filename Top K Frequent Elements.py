from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums=[1,1,1,2,2,3], k=2
        c = Counter(nums)  # Counter({1: 3, 2: 2, 3: 1})
        k_most_common = c.most_common(k)  # [(1, 3), (2, 2)]
        return [element for element, count in k_most_common]  # [1, 2]

print(Solution().topKFrequent([1,1,1,2,2,3],2))