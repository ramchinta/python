'''We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.'''

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        mem={}
        def calculate(l,h):
            if l >= h:  return 0
            if (l,h) not in mem:
                mem[l,h] = min(i+max(calculate(i+1, h), calculate(l, i-1)) for i in range((l+h)>>1, h+1))
            return mem[l,h]

        return calculate(1,n)

print(Solution().getMoneyAmount(1))
#0