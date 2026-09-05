class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dp(i, j):
            if i >= len(nums):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            noTake = dp(i + 1, j)

            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + dp(i + 1, i)

            memo[(i, j)] = max(take, noTake)
            return memo[(i, j)]

        return dp(0, -1)