class Solution:
    def countSeniors(self, details: List[str]) -> int:
        pl = 0
        for x in details:
            if int(x[11:13]) > 60:
                pl +=1
        return pl