class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + bfs(r-1, c) + bfs(r+1, c) + bfs(r, c + 1) + bfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_islands = max(max_islands, bfs(r, c))
        
        return max_islands