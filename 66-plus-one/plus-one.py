class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        total = "".join(str(d) for d in digits)

        totals = int(total) + 1
        plus = [int(char) for char in str(totals)]

        return plus
        