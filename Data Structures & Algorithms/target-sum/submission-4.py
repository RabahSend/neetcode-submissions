class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, remain):
            if (i, remain) in memo:
                return memo[(i, remain)]

            if i == len(nums) and remain == target:
                return 1

            if i >= len(nums):
                return 0

            memo[(i, remain)] = dfs(i + 1, remain + nums[i]) + dfs(i + 1, remain - nums[i])

            return memo[(i, remain)]

        return dfs(0, 0)