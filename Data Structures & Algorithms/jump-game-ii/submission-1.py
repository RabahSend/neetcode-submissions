class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def minJump(i):
            if i >= len(nums) - 1:
                return 0

            if nums[i] == 0:
                return float("inf")

            if i in memo:
                return memo[i]
            
            memo[i] = float("inf")
            for j in range(nums[i]):
                memo[i] = min(memo[i], 1 + minJump(i + j + 1))

            return memo[i]

        
        return minJump(0)