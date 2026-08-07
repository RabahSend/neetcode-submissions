class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        v_s1 = [0] * 26
        v_s2 = [0] * 26
        n = len(s1)

        for i in range(n):
            v_s1[ord(s1[i]) - ord('a')] += 1
            v_s2[ord(s2[i]) - ord('a')] += 1

        if v_s1 == v_s2:
            return True

        for i in range(n, len(s2)):
            v_s2[ord(s2[i - n]) - ord('a')] -= 1
            v_s2[ord(s2[i]) - ord('a')] += 1

            if v_s1 == v_s2:
                return True

        return False
