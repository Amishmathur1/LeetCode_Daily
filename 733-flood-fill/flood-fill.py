class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dq = deque([(sr, sc)])
        row = len(grid)
        col = len(grid[0])

        org_col = grid[sr][sc]
        if org_col == color:
            return grid
        
        grid[sr][sc] = color

        while dq:
            r, c = dq.popleft()            
            for dr, dc in di:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == org_col:
                    grid[nr][nc] = color
                    dq.append((nr,nc))        
        return grid
