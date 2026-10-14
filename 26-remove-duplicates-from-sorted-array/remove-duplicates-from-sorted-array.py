class Solution:
    """ Optimal
    time: o(n)
    space: o(1)
    replace each duplicate with a unique
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1

        return l
            