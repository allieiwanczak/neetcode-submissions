class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        n, m = len(g), len(s)
        happy = 0
        while i<len(g) and j< len(s):
            if s[j] >= g[i]:
                happy +=1
                i+=1
            j+=1
        return happy
