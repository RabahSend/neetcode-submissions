class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        rightIndex = [0] * n

        for i in range(n - 2, -1, -1):
            rightIndex[i] = rightIndex[i + 1] + nums[i + 1]

        leftIndex = 0
        for i in range(n):
            if leftIndex == rightIndex[i]:
                return i

            leftIndex += nums[i]

        return -1

