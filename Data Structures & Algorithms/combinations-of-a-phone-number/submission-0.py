class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        mapping = {
            '2': "abc",
            '3': "def", 
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        def backtrack(current, i_digit):
            if len(current) == len(digits):
                if len(digits) ==0:
                    return
                else:
                    results.append("".join(current[:]))
                    return
            
            avail = list(mapping[digits[i_digit]])
            for i in range(len(avail)):
                current.append(avail[i])
                backtrack(current,i_digit+1)
                current.pop()
    
        backtrack([],0)
        return results