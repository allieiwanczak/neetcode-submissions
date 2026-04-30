class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        if all(char in it for char in s):
            return True
        else:
            return False