class Solution:
    """ Optimal: 
    left = 0
    for i in (1,nums):
        if nums[left]!=nums[i]:
            nums[left]=nums[i]
            left+=1
        else:
            nums.remove(nums[i])
    return len(nums), nums
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(1,len(nums)):
            if nums[left]!=nums[i]:
                left+=1
                nums[left]=nums[i]
        return len(nums[:left+1])
            