class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols = len(matrix), len(matrix[0])
        t = [[] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                t[c].append(matrix[r][c])
        return t
