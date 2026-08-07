class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        sum_nums //= 2

        memo = {}

        def dfs(j, cur_sum):
            if cur_sum == sum_nums:
                return True
                
            if j >= len(nums):
                return False

            if cur_sum > sum_nums:
                return False

            if (j, cur_sum) in memo:
                return memo[(j, cur_sum)]
            
            ignore = dfs(j + 1, cur_sum)
            take = dfs(j + 1, cur_sum + nums[j])

            memo[(j, cur_sum)] = ignore or take

            return memo[(j, cur_sum)]

        return dfs(0,0)