class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = max_l=0
        longest = 0
        char = set()

        for right in range (len(s)):
            while s[right] in char:
                char.remove(s[first])
                first += 1

            char.add(s[right])
            max_l = max(max_l, right - first + 1)
        return max_l