class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1,0],[1,0],[0,-1], [0,1]]
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        count = 0

        def dfs(r,c):
            if r<0 or c<0 or r>= rows or c>= cols:
                return
            if grid[r][c] == "0":
                return
            if visited[r][c]:
                return

            visited[r][c] = True

            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == False:
                    dfs(row,col)
                    count+=1
        return count