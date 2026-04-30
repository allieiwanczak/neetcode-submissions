class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(current, start_i):
            if start_i >= len(nums):
                if current not in results:
                    results.append(current[:])
                    return
            
            for i in range(start_i,len(nums)):
                # include
                current.append(nums[i])
                backtrack(current, i+1)
                current.pop()

                #exclude
                backtrack(current, i+1)

        backtrack([], 0)
        return results
