class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        counts = Counter(s)
        res = []
        left = 0
        many = set()

        for right in range(len(s)):
            counts[s[right]] -= 1

            if counts[s[right]] >= 1:
                many.add(s[right])
                continue

            if counts[s[right]] == 0:
                if s[right] in many:
                    many.remove(s[right])

            if not many:
                res.append(right - left + 1)
                left = right + 1

        return res