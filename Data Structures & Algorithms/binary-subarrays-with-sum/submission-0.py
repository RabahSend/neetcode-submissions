class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        preSum = {0: 1}
        res = 0

        for i in range(len(nums)):
            count += nums[i]

            if count - goal in preSum:
                res += preSum[count - goal]

            preSum[count] = preSum.get(count, 0) + 1

        return res