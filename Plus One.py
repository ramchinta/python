'''Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.'''

class Solution:
    def plusOne(self, digits):
        digits[-1] = digits[-1] + 1
        j = len(digits) - 1
        while j >= 0:
            if digits[j] >= 10 and j>0:
                carry = digits[j] // 10
                digits[j - 1] = digits[j - 1] + carry
                digits[j] = digits[j] % 10
            elif digits[j] >= 10 and j == 0:
                carry = digits[j] // 10
                digits[j] = digits[j] % 10
                digits.insert(0,carry)
            j = j - 1
        if len(digits) > 1:
            return digits
        return digits

print(Solution().plusOne([1,2,3]))
#[1, 2, 4]