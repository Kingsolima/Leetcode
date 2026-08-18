class Solution:
    # Brute force:
    """
    input: int array called nums
    output: return True if any value appears at least twice, else return false

    1. for every element
        2. put it in seen
        3. for every element after that one
            4. if element in seen
                6. return true
    return false

    time: O(n^2)
    space: O(n)
    """

    # Optimal:
    """
    1. sort it
    3. for loop (1,end)
        4. if nums[i-1]==nums[i]:
            return true
    return false
    time: O(nlogn)
    speed: O(n)
    """
    # MOST OPTIMAL
    """
    seen = ()
    for i in range:
        if nums[i] in seen:
            return true
        seend.add(nums[i])

    return false
    time: 
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        