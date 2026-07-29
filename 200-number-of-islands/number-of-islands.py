from functools import lru_cache
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        # @lru_cache(None)
        def dfs(r, c):
            if (r < 0 or r >= row or
                c < 0 or c >= col or 
                grid[r][c] != '1'
            ):
                return 
            
            grid[r][c] = '0'

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
                           
        
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)
        return count