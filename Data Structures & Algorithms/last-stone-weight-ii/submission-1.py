class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if i == len(stones):
                return abs(total)

            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = min(dfs(i + 1, total - stones[i]),
            dfs(i + 1, total + stones[i]))

            return memo[(i, total)]

        return dfs(0, 0)


