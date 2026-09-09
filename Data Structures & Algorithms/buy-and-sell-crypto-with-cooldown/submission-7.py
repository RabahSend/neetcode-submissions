class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, bought):
            if (day, bought) in memo:
                return memo[(day, bought)]

            if day >= len(prices):
                return 0

            cooldown = dp(day + 1, bought)
            if not bought:
                sell = dp(day + 2, not bought) + prices[day]
                memo[(day, bought)] = max(cooldown, sell)
            else:
                buy = dp(day + 1, not bought) - prices[day]
                memo[(day, bought)] = max(cooldown, buy)

            return memo[(day,bought)]

        return dp(0, True)