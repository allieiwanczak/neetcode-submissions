class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] +=1
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

        