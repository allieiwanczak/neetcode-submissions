class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.rstrip()
        s = list(s)
        word = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                word.append(s[i])
            else:
                break
        return len(word)