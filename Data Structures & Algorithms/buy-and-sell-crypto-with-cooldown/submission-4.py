class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, bought):
            if (day, bought) in memo:
                return memo[(day, bought)]

            if day >= len(prices):
                return 0

            if bought == -1:
                memo[(day, bought)] = max(dp(day + 1, bought), dp(day + 1, day))
            else:
                memo[(day, bought)] = max(prices[day] - prices[bought] + dp(day + 2, -1), dp(day + 1, bought))

            return memo[(day,bought)]

        return dp(0, -1)

            