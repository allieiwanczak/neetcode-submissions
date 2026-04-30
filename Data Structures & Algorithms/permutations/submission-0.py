class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = []
        results = []

        def backtrack(current,start_i):
            if len(current) == len(nums):
                results.append(current[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    current.append(nums[i])
                    used.append(nums[i])
                    backtrack(current,i+1)
                    current.pop()
                    used.pop()

        backtrack([],0)
        return results