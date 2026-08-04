class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = []
        
        # Identify unique elements
        for num in nums:
            if num not in unique_elements:
                unique_elements.append(num)
        
        # Modify the original nums array in-place
        for i in range(len(unique_elements)):
            nums[i] = unique_elements[i]
            
        return len(unique_elements)