class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i ,j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                res = min(dp(i, j + 1), dp(i + 1, j))
                res = min(res, dp(i + 1, j + 1)) + 1
                memo[(i, j)] = res

            return memo[(i, j)]

        return dp(0, 0)