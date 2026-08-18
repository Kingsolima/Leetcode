class Solution:
    # brute:
    """
    new_s = sorted(s)
    new_t = sorted(t)

    if len(s)!=len(t):
        return False
    return new_s == new_t

    time: o(mlogm + nlogn)
    space: o(m+n)
    """

    # OPTIMAL:
    """
    new_s = {}
    new_t = {}

    if len(s)!=len(t):
        return False
    
    for i in range(len(s)):
        if s[i] in new_s:
            new_s[s[i]] += 1
        else:
            new_s[s[i]] = 1
        if t[i] in new_t:
            new_t[t[i]] += 1
        else:
            new_t[t[i]] = 1

    return new_t==new_s

    time: O(n)
    space: O(m+n)
        
    """
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = {}
        new_t = {}

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in new_s:
                new_s[s[i]] += 1
            else:
                new_s[s[i]] = 1
            if t[i] in new_t:
                new_t[t[i]] += 1
            else:
                new_t[t[i]] = 1

        return new_t==new_s