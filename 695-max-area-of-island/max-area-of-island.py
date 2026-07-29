class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, area):
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                grid[r][c] != 1
            ):
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in dirs:
                area += dfs(dr + r, dc + c, area)
            return area

        max_area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        return max_area