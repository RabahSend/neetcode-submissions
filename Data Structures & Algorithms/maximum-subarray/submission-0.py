class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float("-inf")
        currSub = float("-inf")

        for num in nums:
            currSub = max(currSub + num, num)
            maxSub = max(currSub, maxSub)

        return maxSub