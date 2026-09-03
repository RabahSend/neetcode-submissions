class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        
        def dfs(i, j):
            if (0 > i or i >= len(grid) or 0 > j or j >= len(grid[0])):
                return False

            if grid[i][j] == "0":
                return False

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += dfs(i, j)

        return count