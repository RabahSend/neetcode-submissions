class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0

            if remain < 0:
                return -1

            if remain in memo:
                return memo[remain]

            minimum = float("inf")          
            for coin in coins:
                result = dfs(remain - coin)

                if result != -1:
                    minimum = min(minimum, result + 1)

            memo[remain] = -1 if minimum == float("inf") else minimum

            return memo[remain]

        return dfs(amount)

            