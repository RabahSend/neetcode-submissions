class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for elem in strs:
            s += str(len(elem)) + "#" + elem 

        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0

        while index < len(s):
            length = 0
            length_str = ""
            char = ''
            char = s[index]
            index += 1
            while char != '#':
                length_str += char
                char = s[index]
                index += 1
            
            length = int(length_str)
            length_str = ""

            for i in range(length):
                length_str += s[i + index]
            
            ans.append(length_str)
            index += length

        return ans

