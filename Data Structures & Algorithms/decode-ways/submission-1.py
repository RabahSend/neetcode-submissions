class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1

            if i in memo:
                return memo[i]

            if int(s[i]) == 0:
                return 0

            memo[i] = dfs(i + 1)

            number = int(s[i:i+2])

            if i < len(s) and 10 <=  number <= 26:
                memo[i] += dfs(i + 2)

            return memo[i]

        return dfs(0)