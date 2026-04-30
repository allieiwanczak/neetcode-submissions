class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = res = 0
        for x in nums:
            if x != 0:
                cnt +=1
                res = max(res, cnt)
            else:
                cnt = 0
        return res