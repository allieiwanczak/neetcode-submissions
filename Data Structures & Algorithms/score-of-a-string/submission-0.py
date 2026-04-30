class Solution:
    def scoreOfString(self, s: str) -> int:
        scores = []    
        for i in range(0, len(s) - 1):
            scores.append(abs(ord(s[i]) - ord(s[i+1])))
        return sum(scores)
