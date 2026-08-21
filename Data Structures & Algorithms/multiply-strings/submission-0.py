class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1int = 0
        for i in range(len(num1) - 1):
            num1int += ord(num1[i]) - ord('0')
            num1int *= 10

        num1int += ord(num1[len(num1) - 1]) - ord('0')

        num2int = 0
        for i in range(len(num2) - 1):
            num2int += ord(num2[i]) - ord('0')
            num2int *= 10

        num2int += ord(num2[len(num2) - 1]) - ord('0')

        return str(num1int * num2int)