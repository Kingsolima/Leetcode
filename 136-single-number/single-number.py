class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1

        return min(seen, key=seen.get)
        