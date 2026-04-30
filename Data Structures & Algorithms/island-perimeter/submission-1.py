class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # p = 6 + (n-2)*2

        rows,cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(r,c, visited):
            p = 0
            if r<0 or c<0 or r>= rows or c>= cols:
                return 1
            if grid[r][c] == 0:
                return 1
            if visited[r][c] == True:
                return 0
            
            visited[r][c] = True

            for dr, dc in directions:
                p+= dfs(r+dr,c+dc, visited)
            return p
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    return dfs(r,c,visited)
        return 0
       

