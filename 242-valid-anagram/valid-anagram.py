class Solution:
    #countS
    #countT
    #
    def isAnagram(self, s: str, t: str) -> bool:
        listS = sorted(s)
        listT = sorted(t)
        return listT == listS