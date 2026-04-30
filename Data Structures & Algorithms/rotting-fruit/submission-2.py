class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque()
        max_min = 0

        #adding all sources
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
        
        #bfs from all
        while queue:
            r,c,dist = queue.popleft()
            max_min = max(max_min,dist)
            
            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0 <= nr<rows and 0<=nc<cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc,dist+1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return max_min