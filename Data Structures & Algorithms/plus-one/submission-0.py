class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = self.createNumber(digits)

        return self.explodeNumber(number + 1)[::-1]


    def createNumber(self, digits: List[int]) -> int:
        number = digits[0]

        for i in range(1, len(digits)):
            number = number * 10 + digits[i]

        return number

    def explodeNumber(self, number: int) -> List[int]:
        digits = []

        while number > 0:
            digits.append(number % 10)
            number //= 10

        return digits