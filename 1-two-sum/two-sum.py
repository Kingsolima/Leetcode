class Solution:
    """(Optimal
    seen={}
    for i in range:
        result = target - nums[i]
        if result in seen:
            return [i, seen[result]]
        seen[i] = i
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in seen:
                return [i, seen[result]]
            seen[nums[i]] = i