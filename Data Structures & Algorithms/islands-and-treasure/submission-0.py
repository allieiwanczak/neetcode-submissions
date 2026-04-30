class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1], [0,1]]
        visited = [[False] * cols for _ in range(rows)]
        inf = 2147483647
        queue =deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
        
        while queue:
            r,c,dist = queue.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0 <= nr<rows and 0<=nc<cols:
                    if grid[nr][nc] == inf:
                        grid[nr][nc] = dist+1
                        queue.append((nr,nc,dist+1))


            


