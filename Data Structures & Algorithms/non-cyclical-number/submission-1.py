class Solution:
    def isHappy(self, n: int) -> bool:
        def numberOfSquares(i):
            count = 0
            while i > 0:
                digit = i % 10
                count += digit * digit
                i //= 10

            return count

        slow, fast = n, numberOfSquares(n)

        while slow != fast:
            slow = numberOfSquares(slow)
            fast = numberOfSquares(numberOfSquares(fast))
        return True if fast == 1 else False