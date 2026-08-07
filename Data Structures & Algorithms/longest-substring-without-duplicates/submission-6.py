class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        res = 0

        path = set()

        while right < len(s):
            while s[right] in path:
                path.remove(s[left])
                left += 1
                
            path.add(s[right])
            right += 1

            res = max(res, len(path))

        return res

        