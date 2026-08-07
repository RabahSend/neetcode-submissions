class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        maxHeightL = 0
        maxHeightR = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxHeightL:
                    maxHeightL = height[left]
                else:
                    ans += maxHeightL - height[left]
                left += 1
            else:
                if height[right] >= maxHeightR:
                    maxHeightR = height[right]
                else:
                    ans += maxHeightR - height[right]
                right -= 1

        return ans