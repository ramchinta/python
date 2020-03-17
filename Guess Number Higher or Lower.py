'''We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

import random
class Solution:
    def guess(self,num):
        chosen = 7
        if chosen == num:
            return 0
        elif chosen > num:
            return 1
        else:
            return -1

    def guessNumber(self, n: int) -> int:
        s=1
        e=n
        while s<=e:
            mid=(e-s)//2+s
            tem=self.guess(mid)
            if tem==0:
                return mid
            elif tem==1:
                s=mid+1
            else:
                e=mid-1
        return

print(Solution().guessNumber(10))
