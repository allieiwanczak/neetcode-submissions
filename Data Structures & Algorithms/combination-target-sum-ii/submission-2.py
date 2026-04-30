class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results =[]
        candidates.sort()

        def backtrack(current,start_i):
            if sum(current) == target:
                results.append(current[:])
                return

            for i in range(start_i, len(candidates)):
                if sum(current) + candidates[i] > target:
                    break
                if i > start_i and candidates[i] == candidates[i-1]:
                    continue
                current.append(candidates[i])
                backtrack(current, i+1)
                current.pop()

        backtrack([],0)
        return results