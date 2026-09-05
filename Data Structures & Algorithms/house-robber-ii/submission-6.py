class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 = {}
        memo2 = {}

        if len(nums) == 1:
            return nums[0]

        def dp(i, end, memo):
            if i in memo:
                return memo[i]

            if i >= end:
                return 0

            memo[i] = max(nums[i] + dp(i + 2, end, memo), dp(i + 1, end, memo))
            return memo[i]

        return max(dp(0, len(nums) - 1, memo1), dp(1, len(nums), memo2))