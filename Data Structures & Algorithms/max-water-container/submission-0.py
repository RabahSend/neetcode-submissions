class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            ans = max(ans, height * width)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return ans
