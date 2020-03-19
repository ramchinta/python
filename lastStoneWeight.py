class Solution:
    def lastStoneWeight(self, stones):

        while len(stones) > 1:
            fmax = max(stones)
            stones.remove(fmax)
            smax = max(stones)
            stones.remove(smax)

            if fmax - smax:
                stones.append(fmax - smax)

        return stones[0] if stones else 0

print(Solution().lastStoneWeight([2,7,4,1,8,1]))
#1