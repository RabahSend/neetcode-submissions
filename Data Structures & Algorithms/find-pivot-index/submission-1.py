class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        n = len(nums)

        for i in range(n):
            rightSum = total - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            leftSum += nums[i]

        return -1
