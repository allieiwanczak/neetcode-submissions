class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        avail = {x: nums.count(x) for x in nums}

        def backtrack(current, start_i):
            if len(current) <= len(nums) and sorted(current) not in results:
                results.append(sorted(current[:]))

            if len(current) > len(nums):
                return
            
            for i in range(start_i, len(nums)):
                current.append(nums[i])
                avail[nums[i]] -=1
                backtrack(current,i+1)
                avail[nums[i]]+=1
                current.pop()
        backtrack([],0)
        return results