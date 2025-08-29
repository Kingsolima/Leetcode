class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_word = list(s)
        t_word = list(t)
        s_word.sort()
        t_word.sort()

        return s_word == t_word