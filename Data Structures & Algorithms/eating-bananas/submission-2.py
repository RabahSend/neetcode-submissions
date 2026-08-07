class Solution:
    def numberOfHours(self, piles, k):
        numHours = 0

        for i in range(len(piles)):
            num = piles[i] // k

            if piles[i] % k != 0:
                num += 1

            numHours += num

        return numHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = max(piles)

        left = 1
        right = min_k

        while left <= right:
            mid_k = (right + left) // 2

            if self.numberOfHours(piles, mid_k) <= h:
                min_k = mid_k
                right = mid_k - 1
            else:
                left = mid_k + 1

        return min_k
