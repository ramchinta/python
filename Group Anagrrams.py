import collections
class Solution(object):
    def groupAnagrams( strs):
        ans = collections.defaultdict(list)
        print(ans)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
            print(ans)
        return ans.values()
print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))