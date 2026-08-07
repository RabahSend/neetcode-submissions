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

            for j in range(i, len(nums)):
                if dfs(j + 1, result + nums[j]):
                    memo[(i, result)] = True
                    return memo[(i, result)]

            memo[(i, result)] = False
            return memo[(i, result)]

        return dfs(0, 0)        

            