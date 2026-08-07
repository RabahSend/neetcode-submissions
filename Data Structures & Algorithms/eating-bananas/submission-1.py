class Solution:
    def numberofHours(self, piles: List[int], k: int) -> int:
        total = 0
        for bananas in piles:
            hours = bananas // k

            if bananas % k != 0:
                hours += 1
            
            total += hours

        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        optimal_k = max_k

        while min_k <= max_k:
            mid = (max_k + min_k) // 2
            hForK = self.numberofHours(piles, mid)

            if hForK > h:
                min_k = mid + 1
            else:
                optimal_k = mid
                max_k = mid - 1

        return optimal_k
