'''Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions
(north, east, west, south).



Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation:
The path with the maximum score is highlighted in yellow.
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3


Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9'''

import heapq
class Solution:
    def maximumMinimumPath(self, A):
        R, C = len(A),len(A[0])
        visited = [[0]*C for _ in range(R)]
        q = [(-A[0][0],0,0)]
        visited[0][0] = 1
        res = A[0][0]
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            v, x, y = heapq.heappop(q)
            if x == R-1 and y == C - 1:
                return -v
            for xd,yd in dirs:
                Cx = x + xd
                Cy = y + yd
                if 0<=Cx<R and 0<=Cy<C and not visited[Cx][Cy]:
                    visited[Cx][Cy] = 1
                    heapq.heappush(q,(max(v,-A[Cx][Cy]),Cx,Cy))

print(Solution().maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]))
#4