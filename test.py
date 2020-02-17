import collections


def numberAmazonTreasureTrucks(rows, column, grid):
    queue = collections.deque()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 1:
                queue.append((r, c))

    def neighbours(r, c):
        for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
            if 0 <= nr < rows and 0 < nc < column:
                yield nr, nc

    count = 0
    while queue:
        r, c = queue.popleft()
        for nr, nc in neighbours(r, c):
            if grid[nr][nc] == 1:
                count = count + 1

    return count


print(numberAmazonTreasureTrucks(5,4,[[1,1,0,0],[0,0,1,0],[0,0,0,0],[1,0,1,1],[1,1,1,1]]))