class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        results = []

        def backtrack(row,col, i):
            if i == len(word):
                return True
            if row <0 or col<0 or row>=len(board) or col>=len(board[0]):
                return False
            if board[row][col] != word[i]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            
            #rest
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                new_row = row+dr
                new_col = col+dc
                if backtrack(new_row,new_col,i+1):
                    return True
            board[row][col] =temp
            return False
        #first letter
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        return False