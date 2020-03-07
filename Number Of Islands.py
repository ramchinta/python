'''Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3'''


class Solution:
    def __init__(self):
        pass

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = (i, j)

                    islands += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] != '0':

                    if self.join_up((i, j), grid):
                        islands -= 1
                    if self.join_left((i, j), grid):
                        islands -= 1

        return islands

    def join_up(self, island, grid):
        i, j = island

        if i - 1 >= 0 and grid[i - 1][j] != '0':
            root1 = self.find_root(grid[i - 1][j], grid)
            root2 = self.find_root(grid[i][j], grid)
            if root1 != root2:
                x, y = root2
                grid[x][y] = root1
                return True

        return False

    def join_left(self, island, grid):
        i, j = island

        if j - 1 >= 0 and grid[i][j - 1] != '0':
            root1 = self.find_root(grid[i][j - 1], grid)
            root2 = self.find_root(grid[i][j], grid)
            if root1 != root2:
                x, y = root2
                grid[x][y] = root1
                return True

        return False

    def find_root(self, island, grid):
        x, y = island
        if grid[x][y] != island:
            grid[x][y] = self.find_root(grid[x][y], grid)
        return grid[x][y]

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
#1