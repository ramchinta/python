import collections
class Solution:
    def mostCommonWord(paragraph, banned):
        banset = set(banned)
        for c in "!?,.';":
            paragraph = paragraph.replace(c," ")
        count = collections.Counter(word for word in paragraph.lower().split())
        ans,best = '',0
        for word in count:
            if count[word] > best and word not in banset:
                ans,best = word,count[word]
        return ans

print(Solution.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit by bob.',['the']))