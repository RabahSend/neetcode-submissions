class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        res = ""

        def dfs(i, j):
            if i >= j:
                return True

            if (i,j) in memo:
                return memo[(i,j)]

            if s[i] != s[j]:
                return False

            memo[(i,j)] = dfs(i + 1, j - 1)

            return memo[(i,j)]

        for j in range(len(s)):
            for i in range(j + 1):
                if dfs(i, j):
                    if len(s[i:j+1]) > len(res):
                        res = s[i:j+1]


        return res