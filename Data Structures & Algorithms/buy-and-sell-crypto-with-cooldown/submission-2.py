class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(day, bought):
            if day >= len(prices):
                return 0

            if (day, bought) in memo:
                return memo[(day, bought)]

            profit = 0
            if bought:
                profit = max(
                    prices[day] + dfs(day + 2, False),
                    dfs(day + 1, True)
                    )
            else:
                profit = max(
                    -prices[day] + dfs(day + 1, True),
                    dfs(day + 1, False)
                )

            memo[(day, bought)] = profit

            return memo[(day, bought)]

        return dfs(0, False)