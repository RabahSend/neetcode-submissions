class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0

        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                ans = max(ans, prices[right] - prices[left])
            
            else:
                left = right
        
        return ans