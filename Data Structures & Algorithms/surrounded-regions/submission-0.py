class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[False] * cols for _ in range(rows)]
        queue = deque()

        # add neighbor cells
        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0,c))
                board[0][c] = "S"
            if board[rows-1][c] == "O":
                queue.append((rows-1,c))
                board[rows-1][c] = "S"
        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r,0))
                board[r][0] = "S"
            if board[r][cols-1] == "O":
                queue.append((r,cols-1))
                board[r][cols-1] = "S"

        # bfs - change neighbors of Os to safe
        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0<=nr<rows and 0<=nc<cols:
                    if board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"

        