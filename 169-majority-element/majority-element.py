class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for i in range(len(nums)):
            if nums[i] not in majority:
                majority[nums[i]] = 1
            else:
                majority[nums[i]] += 1
        
        max_value = max(majority, key=majority.get)

        return max_value
        