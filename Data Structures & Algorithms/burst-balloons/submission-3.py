class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        def dfs(current):
            
            if current in memo:
                return memo[current]

            memo[current] = 0
            for i in range(len(current)):
                prev_balloon = 1 if i - 1 < 0 else current[i - 1]
                next_balloon = 1 if i + 1 >= len(current) else current[i + 1]
                coins = prev_balloon * current[i] * next_balloon
                remain = current[:i] + current[i + 1:]
                memo[current] = max(memo[current], coins + dfs(remain))

            return memo[current]

        return dfs(tuple(nums))