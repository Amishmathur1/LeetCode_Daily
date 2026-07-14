class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque([])
        cnt = 0

        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    cnt += 1
                if grid[r][c] == 2:
                    dq.append((r,c))
        
        if cnt == row*col:
            return 0

        count = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            size = len(dq)
            count += 1

            for _ in range(size):
                r, c = dq.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    if (nr < 0 or nr >= row or
                        nc < 0 or nc >= col or
                        grid[nr][nc] != 1):
                        continue

                    grid[nr][nc] = 2
                    dq.append((nr, nc))
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
        
        return count - 1