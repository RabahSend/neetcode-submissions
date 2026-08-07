class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == j:
                memo[(i, j)] = nums[i]
            else:
                memo[(i, j)] = dfs(i - 1, j) * nums[i]

            return memo[(i, j)]

        
        for i in range(len(nums)):
            for j in range(i + 1):
                dfs(i, j)

        return max(memo.values())

            