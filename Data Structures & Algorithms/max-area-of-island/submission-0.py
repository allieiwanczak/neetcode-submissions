class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            if visited[r][c]:
                return 0
            
            visited[r][c] = True
            area = 1
            for dr, dc in directions:
                area += dfs(dr+r,c+dc)
            return area
        
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == 1:
                    max_area = max(max_area, dfs(row,col))
        return max_area