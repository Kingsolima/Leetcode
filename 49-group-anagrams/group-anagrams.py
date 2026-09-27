class Solution:
    """ Brute
    defaultdict
    for s loop
        join the sorted word
        result.append sorted
    return list(result.values())
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorts = "".join(sorted(s))
            result[sorts].append(s)
        return list(result.values())
        