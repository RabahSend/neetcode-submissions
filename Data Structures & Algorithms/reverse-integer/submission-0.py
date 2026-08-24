class Solution:
    def reverse(self, x: int) -> int:
        def rec(n, rev):
            if n == 0:
                return rev

            rev = rev * 10 + n % 10
            return rec(n // 10, rev)

        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_num = rec(x, 0)
        reversed_num *= sign

        if not (-(1 << 31) < reversed_num < (1 << 31) - 1):
            return 0

        return reversed_num
