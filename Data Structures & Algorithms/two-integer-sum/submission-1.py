class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, val in enumerate(nums):
            if target - val not in prevMap:
                prevMap[val] = i
            else:
                return [prevMap[target-val], i]