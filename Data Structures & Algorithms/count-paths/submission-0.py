class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if j >= n or i >= m:
                return 0

            if j == n - 1 and i == m - 1:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = dfs(i + 1, j) + dfs(i, j + 1)

            return memo[(i,j)]

        return dfs(0,0)

            