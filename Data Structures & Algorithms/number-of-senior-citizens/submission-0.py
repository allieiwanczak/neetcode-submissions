class Solution:
    def countSeniors(self, details: List[str]) -> int:
        pl = []
        for x in details:
            if int(x[11:13]) > 60:
                pl.append(x)
        return len(pl)