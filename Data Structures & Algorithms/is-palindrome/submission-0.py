class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(s) - 1
        
        print(s)

        for i in range(len(s)):
            if(s[i] != s[n]):
                return False
            n -= 1

        return True