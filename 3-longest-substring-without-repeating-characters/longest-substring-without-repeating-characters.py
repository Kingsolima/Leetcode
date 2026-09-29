class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_set = 0
        seen = set()
        while r < len(s):
            current_set = 0
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                current_set+=1
                r+=1
            
            longest_set = max(longest_set, r - l)

            if r < len(s):          # stopped on a duplicate
                seen.remove(s[l])
                l += 1
        return longest_set

        # time: o(nlogn)
        # space: o(n)