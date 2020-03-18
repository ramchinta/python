'''Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue,
and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.
Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n,
where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors
alternate along the path (or -1 if such a path doesn't exist).



Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]


Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n'''


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):

        adj = {i: [] for i in range(n)}

        for u, v in red_edges:
            adj[u].append((v, 0))  # 0 indicates red
        for u, v in blue_edges:
            adj[u].append((v, 1))  # 1 indicates blue

        # bfs distance
        dist = [-1 for _ in range(n)]
        visited = set()

        dist[0] = 0

        q = [(0, -1)]  # -1 color for initial
        ct = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                u, c = q.pop(0)
                if n * c + u in visited:
                    continue
                if dist[u] == -1:
                    dist[u] = ct
                visited.add(n * c + u)
                for v, next_c in adj[u]:
                    if next_c != c:
                        q.append((v, next_c))
            ct += 1
        return dist

print(Solution().shortestAlternatingPaths(3,[[0,1],[1,2]],[]))
#[0,1,-1]