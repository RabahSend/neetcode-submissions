class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {0: 1}

        def dfs(remain):
            if remain in memo:
                return memo[remain]

            if remain < 0:
                return 0

            res = 0
            for num in nums:
                res += dfs(remain - num)

            memo[remain] = res

            return memo[remain]

        return dfs(target)