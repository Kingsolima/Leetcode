class Solution:
    # Brute force:
    """
    seen={}
    for loop:
        if nums[i] in seen:
            return true
        seen[nums[i]] = 1
    
    return False

    Time: O(n)
    Space: O(n)
    """

    # Optimal:
    """
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = 1
        return False
        