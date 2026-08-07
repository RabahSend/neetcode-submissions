class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def bfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == "0"):
                return

            grid[r][c] = "0"
            bfs(r-1, c)
            bfs(r+1, c)
            bfs(r, c-1)
            bfs(r, c+1)


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands