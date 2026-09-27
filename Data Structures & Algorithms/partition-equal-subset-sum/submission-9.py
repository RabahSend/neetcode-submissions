class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)

        if sumNums % 2 != 0:
            return False

        target = sumNums / 2

        memo = {}

        def dfs(i, total):
            nonlocal target

            if (i, total) in memo:
                return memo[(i, total)]

            if i == len(nums):
                if total == target:
                    return True
                return False

            memo[(i, total)] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
            return memo[(i, total)]

        return dfs(0, 0)

