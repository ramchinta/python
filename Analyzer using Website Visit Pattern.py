'''We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
(The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution,
return the lexicographically smallest such 3-sequence.



Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.'''
import collections
class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        hashmap = collections.defaultdict(set)
        userset = set(username)
        n = len(username)

        # combine the information and sort by time O(n)
        info = []
        for i in range(n):
            info.append([timestamp[i], username[i], website[i]])
        info.sort()

        # for each user record the sequence O(n * unique user)
        for name in userset:
            visit = []
            counter = 0
            for i in range(n):
                if info[i][1] != name:
                    continue
                visit.append(info[i][2])
                counter += 1
            # 3 sequence O(n3)
            for i in range(counter - 2):
                for j in range(i + 1, counter - 1):
                    for k in range(j + 1, counter):
                        hashmap[(visit[i], visit[j], visit[k])].add(name)

        # processing recorded visit O(unique seq)
        ans_list = []
        for seq in hashmap:
            ans_list.append([-len(hashmap[seq]), seq])
        ans_list.sort()

        # extract ans
        return ans_list[0][1]

print(Solution().mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"],[1,2,3,4,5,6,7,8,9,10],["home","about","career","home","cart","maps","home","home","about","career"]))
#('home', 'about', 'career')