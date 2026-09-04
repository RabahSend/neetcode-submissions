class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = maxLength = currentNumZero = 0

        for right in range(len(nums)):
            currentNumZero += 1 if nums[right] == 0 else 0

            while left <= right and currentNumZero > k:
                currentNumZero -= 1 if nums[left] == 0 else 0
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength