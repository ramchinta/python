'''Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive.  The answer is in lowercase.'''

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