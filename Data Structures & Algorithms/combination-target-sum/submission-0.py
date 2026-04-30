class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(current, start_i):
            if sum(current) == target and current not in result:
                result.append(current[:])
                return
            
            for i in range(start_i,len(nums)):
                if sum(current) + nums[i] <= target:
                    current.append(nums[i])
                    backtrack(current,i)
                    current.pop()

        backtrack([],0)
        return result
            