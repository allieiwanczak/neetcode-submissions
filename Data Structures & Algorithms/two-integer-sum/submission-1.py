class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, x in enumerate(nums):
            needed = target - x
            if needed in dict:
                return [dict[needed], i]
            else:
                dict[x] = i