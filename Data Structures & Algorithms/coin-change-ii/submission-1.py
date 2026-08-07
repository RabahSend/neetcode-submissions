class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remain):
            if remain < 0 or i >= len(coins):
                return 0

            if remain == 0:
                return 1

            if (i, remain) in memo:
                return memo[(i, remain)]

            memo[(i, remain)] = dfs(i, remain - coins[i]) + dfs(i + 1, remain)

            return memo[(i, remain)]

        return dfs(0, amount)