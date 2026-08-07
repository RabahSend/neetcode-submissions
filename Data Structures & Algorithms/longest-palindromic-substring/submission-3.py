class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}

        def dfs(left, right):
            if left >= right:
                return True

            if (left, right) in memo:
                return memo[(left,right)]

            if s[right] != s[left]:
                memo[(left,right)] = False
            else:
                memo[(left,right)] = dfs(left+1, right-1)

            return memo[(left,right)]

        res = s[0]

        for left in range(len(s)):
            for right in range(left, len(s)):
                if dfs(left,right) and (right - left + 1) >= len(res):
                    res = s[left:right+1]

        return res

        