class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = set(nums)
        counters = {list(keys)[i]:0 for i in range(len(keys))}
        for value in nums:
            
            counters[value] += 1
        
            if counters[value] > 1:
                return True

        return False
         