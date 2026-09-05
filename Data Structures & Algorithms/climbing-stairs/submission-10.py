class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return 1

            memo[i] = dp(i + 1) + dp(i + 2)

            return memo[i]

        return dp(1)