class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        dq = deque([])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dq.append((i,j))
                
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        while dq:
            r, c = dq.popleft()

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if (nr >= row or nr < 0 or
                    nc >= col or nc < 0 or 
                    grid[nr][nc] == 0
                ):
                    count += 1

        return count         
