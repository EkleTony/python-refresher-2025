"""=========Number of Islands - Leetcode 200 - Graphs (Python)
 """

from collections import deque


class Solution:
    def numIsland(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        num_island = 0

        def bfs(r, c):
            # using a queue
            queue = deque([(r, c)])
            grid[r][c] = "0"  # marked visited
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()  # remove recent cell
                # need to traverse

                for dr, dc in direction:
                    nr = row + dr
                    nc = col + dc

                    # checking for range imbalance before appending to my queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"

        def dfs(r, c):
            # checking edge cases
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            else:
                grid[r][c] = "0"
                dfs(r+1, c)  # down
                dfs(r-1, c)  # up
                dfs(r, c+1)  # right
                dfs(r, c-1)  # left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_island += 1
                    dfs(r, c)
                    # bfs(r, c)

        return num_island
