class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        memo[0] = 1
        memo[1] = 1

        def dp(i):
            if memo[i] != 0:
                return memo[i]

            if i == 0:
                return 1

            if i < 0:
                return 0

            memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]

        return dp(n)