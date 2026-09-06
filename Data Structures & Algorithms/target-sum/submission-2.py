class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, remain):
            if (i, remain) in memo:
                return memo[(i, remain)]

            if i >= len(nums):
                return remain == target

            memo[(i, remain)] = dp(i + 1, remain + nums[i]) + dp(i + 1, remain - nums[i])

            return memo[(i, remain)]

        return dp(0, 0)