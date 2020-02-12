'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


class Solution:
    def twoSum(nums, target):
        a = {}
        for i, j in enumerate(nums):
            remaining = target - j
            if remaining in a:
                return [a[remaining], i]
            else:
                a[j] = i

print(Solution.twoSum([2,7,11,15],26))