class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remain):
            if remain < 0:
                return 0

            if remain == 0:
                return 1

            if (i, remain) in memo:
                return memo[(i, remain)]

            result = 0
            for k in range(i, len(coins)):
                result += dfs(k, remain - coins[k])

            memo[(i, remain)] = result

            return memo[(i, remain)]

        return dfs(0, amount)