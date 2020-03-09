'''Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.'''

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
#[1, 2]