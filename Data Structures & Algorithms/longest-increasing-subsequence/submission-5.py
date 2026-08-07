class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i,j):
            if j >= len(nums):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            ignore = dfs(i, j + 1)

            take = 0
            if i == -1 or nums[i] < nums[j]:
                take = 1 + dfs(j, j + 1)

            memo[(i,j)] = max(ignore, take)

            return memo[(i,j)]

        return dfs(-1, 0)