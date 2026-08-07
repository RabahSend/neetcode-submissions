class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in s[left:right]:
                max_length = max(max_length, right - left)

                while s[right] in s[left:right]:
                    left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
