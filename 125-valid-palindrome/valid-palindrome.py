class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. for loop
            2.only alphanumeric letters
            3. strip all spaces
        4. return new_s==reversed_s

        unoptimal
        time: o(n)
        space: o(n)
        """
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1]