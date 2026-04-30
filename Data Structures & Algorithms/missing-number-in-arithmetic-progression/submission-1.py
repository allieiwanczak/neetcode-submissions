class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[n-1] - arr[0])//n
        lo, high = 0, n-1
        while lo<high:
            mid = (lo+high) //2
            if arr[mid] == arr[0] + mid*diff:
                lo = mid+1
            else:
                high = mid
        return arr[0] + lo*diff