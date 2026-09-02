class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        windowSize = len(cardPoints) - k

        if windowSize == 0:
            return sum(cardPoints)

        currentCount = left = 0
        minimumCount = float("inf")
        
        for right in range(len(cardPoints)):
            currentCount += cardPoints[right]

            if right - left >= windowSize - 1:
                minimumCount = min(minimumCount, currentCount)
                currentCount -= cardPoints[left]
                left += 1

        return sum(cardPoints) - minimumCount
