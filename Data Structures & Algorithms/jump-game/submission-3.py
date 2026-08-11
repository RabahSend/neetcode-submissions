class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def jump(i):
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            if i in memo:
                return memo[i]

            for j in range(nums[i]):
                if jump(i + j + 1):
                    memo[i] = True
                    return memo[i]
            
            memo[i] = False
            return memo[i]

        return jump(0)