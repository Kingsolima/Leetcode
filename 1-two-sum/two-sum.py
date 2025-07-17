class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # start j at i+1 to avoid duplicate pairs
                if nums[i] + nums[j] == target:
                    return [i, j]  # return immediately when found

            