class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        res = 0

        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
                right = left
            else:
                right += 1

            res = max(res, right - left)

        return res

        