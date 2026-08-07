class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            ans = max(ans, (min(heights[right], heights[left]) * (right - left)))

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return ans