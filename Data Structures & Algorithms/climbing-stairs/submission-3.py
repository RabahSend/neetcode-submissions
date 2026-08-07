class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(steps: int) -> int:
            if steps <= 2:
                return steps

            if steps in memo:
                return memo[steps]

            memo[steps] = dp(steps-1) + dp(steps-2)
            return memo[steps]

        return dp(n)