class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Create a set from the list
        set_of_unique = set(nums)

        return len(set_of_unique) != len(nums)