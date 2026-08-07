class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, j, bought):
            if j >= len(prices) or i >= len(prices):
                return 0

            if (i,j, bought) in memo:
                return memo[(i,j, bought)]

            profit = 0
            if bought:
                profit = max(
                    prices[j] - prices[i] + dfs(j + 2, j + 3, False),
                    dfs(i, j + 1, True)
                    )
            else:
                profit = max(
                    dfs(i, j, True),
                    dfs(i + 1, i + 1, False)
                )

            memo[(i,j, bought)] = profit

            return memo[(i,j, bought)]

        return dfs(0, 1, False)