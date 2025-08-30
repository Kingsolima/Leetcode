import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(re.sub(r'[^A-Za-z0-9]', '', s).lower())
        r = s[:]          # make a copy
        r.reverse()       # in-place reverse on the copy
        return s == r
        