from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        memo = {}

        def dfs(left: int, right: int) -> int:
            # No balloon exists strictly between the boundaries.
            if left + 1 == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            result = 0

            # Choose the balloon that will be burst last
            # inside the interval (left, right).
            for k in range(left + 1, right):
                coins = (
                    balloons[left] * balloons[k] * balloons[right]
                    + dfs(left, k)
                    + dfs(k, right)
                )

                result = max(result, coins)

            memo[(left, right)] = result
            return result

        return dfs(0, len(balloons) - 1)