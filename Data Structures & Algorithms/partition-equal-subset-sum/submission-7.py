class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        sum_nums //= 2

        memo = {}

        def dfs(i, result):
            if i >= len(nums):
                return False

            if result == sum_nums:
                return True

            if (i,result) in memo:
                return memo[(i,result)]

            take = dfs(i + 1, result + nums[i])
            ignore = dfs(i + 1, result)

            memo[(i, result)] = take or ignore
            
            return memo[(i, result)]

        return dfs(0, 0)        

            