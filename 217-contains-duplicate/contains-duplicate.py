class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        bob = set()
        for i in nums:
            if i in bob:
                return True
            bob.add(i)
        return False
        