class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        count = 0

        def dfs(i, j):
            if i >= j:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]

            if s[i] != s[j]:
                return 0

            memo[(i,j)] = dfs(i+1, j-1)

            return memo[(i,j)]

        for j in range(len(s)):
            for i in range(j + 1):
                count += dfs(i,j)

        return count