class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotate by 90deg everse and transpose
        n = len(matrix)

        matrix.reverse()

        for r in range(n):
            for c in range(r+1,n):
                matrix[c][r], matrix[r][c] = matrix[r][c],matrix[c][r]

        