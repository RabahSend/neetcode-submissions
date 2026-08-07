class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            ignoretext1 = dfs(i + 1, j)
            ignoretext2 = dfs(i, j + 1)

            take = 0
            if text1[i] == text2[j]:
                take = 1 + dfs(i+1,j+1)

            memo[(i,j)] = max(max(ignoretext1, ignoretext2), take)

            return memo[(i,j)]

        return dfs(0,0)
                