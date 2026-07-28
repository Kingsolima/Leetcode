class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in range(len(s)):
            if s[i].isalnum():
                a.append(s[i].lower())
        return a==a[::-1]
                