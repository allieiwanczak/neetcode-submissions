class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        atl_visited = [[False] * cols for _ in range(rows)]
        pac_visited = [[False] * cols for _ in range(rows)]

        res = []

        # pac
        queue = deque()
        for c in range(cols):
            queue.append((0,c))
            pac_visited[0][c] = True
        for r in range(rows):
            queue.append((r,0))
            pac_visited[r][0] = True
        
        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc
            
                if 0<=nr<rows and 0<= nc<cols:
                    if not pac_visited[nr][nc] and heights[r][c] <= heights[nr][nc]:
                        pac_visited[nr][nc] = True
                        queue.append((nr,nc))
        
        #alt
        queue = deque()
        for c in range(cols):
            queue.append((rows-1,c))
            atl_visited[rows-1][c] = True
        for r in range(rows):
            queue.append((r,cols-1))
            atl_visited[r][cols-1] = True
        
        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc
            
                if 0<=nr<rows and 0<= nc<cols:
                    if not atl_visited[nr][nc] and heights[r][c] <= heights[nr][nc]:
                        atl_visited[nr][nc] = True
                        queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if pac_visited[r][c] == True and atl_visited[r][c] == True:
                    res.append([r,c])
        return res



