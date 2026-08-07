class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, total_sum):
            if total_sum == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            if (i, total_sum) in memo:
                return memo[(i, total_sum)]

            memo[(i, total_sum)] = dfs(i + 1, total_sum + nums[i]) + dfs(i + 1, total_sum - nums[i])

            return memo[(i, total_sum)]

        return dfs(0, 0)