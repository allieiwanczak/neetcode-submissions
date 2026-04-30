class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for x in s:
            count_s[x] = count_s.get(x, 0) + 1
        for x in t:
            count_t[x] = count_t.get(x, 0) + 1
        if count_s == count_t:
            return True
        else:
            return False