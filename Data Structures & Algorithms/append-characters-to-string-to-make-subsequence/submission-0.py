class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        needed = []
        it = iter(s)
        for char in t:
            if char in it:
                continue
            else:
                needed.append(char)
        return len(needed)