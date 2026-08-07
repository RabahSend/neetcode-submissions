class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m = [0] * 26

        for i in range (0, len(s)):
            m[ord(s[i]) - ord('a')] += 1
            m[ord(t[i]) - ord('a')] -= 1
            
        if m == [0] * 26:
            return True
        
        return False