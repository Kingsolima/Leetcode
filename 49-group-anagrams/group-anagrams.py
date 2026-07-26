class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        total = []
        for i in range(len(strs)):
            new = sorted(strs[i])          # note: sorted() on a string returns a list, so...
            new = ''.join(new)             # ...join it back, since a list can't be a dict key
            if new in group:
                group[new].append(strs[i])
            else:
                group[new] = [strs[i]]     # <- initialize WITH the current string
        for key in group:
            total.append(group[key])
        return total