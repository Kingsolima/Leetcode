class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # We will use a nested for loop to solve this. By having the first for loop to go through one by one in nums and each time going through the nested for loop to see if it adds up to the target

        for left in range(len(nums)):
            for right in range(left+1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]
        return False
