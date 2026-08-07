class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        
        left = 0
        best_start = 0
        best_length = float("inf")
        needed = {}
        have = {}

        for char in t:
            needed[char] = needed.get(char, 0) + 1

        def is_valid():
            for char in needed:
                if have.get(char, 0) < needed[char]:
                    return False
            return True

        for right in range(len(s)):
            have[s[right]] = have.get(s[right], 0) + 1

            while is_valid():
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_start = left
                have[s[left]] -= 1
                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]
                 