class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in range (len(s)):
            if s[i].isalnum():
                 a.append(s[i].lower()) 
        
        # Fix: Use slicing to get a reversed copy
        return a == a[::-1] 
