'''Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.'''

from math import e, log

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
print(Solution().mySqrt(25))
#5