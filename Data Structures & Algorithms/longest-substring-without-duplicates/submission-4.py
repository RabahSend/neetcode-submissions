class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        res = 0

        path = set()

        while right < len(s):
            if s[right] in path:
                path.clear()
                left += 1
                right = left
            else:
                path.add(s[right])
                right += 1

            res = max(res, len(path))

        return res

        