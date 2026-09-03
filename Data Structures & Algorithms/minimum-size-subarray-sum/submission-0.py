class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSum = float("inf")
        currentSum = left = 0

        for right in range(len(nums)):
            currentSum += nums[right]
            
            while currentSum >= target:
                minSum = min(minSum, right - left + 1)
                currentSum -= nums[left]
                left += 1

        return minSum if minSum != float("inf") else 0