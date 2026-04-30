class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(current,open,close):
            if len(current) == 2*n:
                if open == n and close== n:
                    results.append("".join(current[:]))
                    return

            if open < n:
                current.append("(")
                backtrack(current,open+1,close)
                current.pop()
            
            if close<open:
                current.append(")")
                backtrack(current,open,close+1)
                current.pop()
        backtrack([],0,0)
        return results