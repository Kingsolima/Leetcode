class Solution:
    # Optimal:
    """
    left = 0
    for loop:
        if nums[left]!=nums[i]:
            left+=1
        else:
            return True
    Return False
    Time: O(n)
    Space: O(1)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        left = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[left]==nums[i]:
                return True
            else:
                left+=1
        return False