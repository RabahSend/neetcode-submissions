class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        res = float("inf")
        right = max(piles)

        def eatBananas(rate):
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / rate)

            return hours

        while left <= right:
            mid = (left + right) // 2

            candidate = eatBananas(mid)

            if candidate > h:
                left = mid + 1
            else:
                right = mid - 1
                res = min(res, mid)

        return res