class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            value = target-nums[i]
            if (value) in seen:
                return [nums.index(value), i]
            seen[nums[i]] = 1