class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        res = 0

        def dfs(left, right):
            if left > right:
                return 1

            if (left, right) in memo:
                return memo[(left, right)]

            if s[left] != s[right]:
                memo[(left,right)] = 0
            else:
                memo[(left,right)] = dfs(left+1, right-1)

            return memo[(left,right)]



        for left in range(len(s)):
            for right in range(left, len(s)):
                res += dfs(left, right)

        return res