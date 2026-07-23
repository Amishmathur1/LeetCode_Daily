class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])
        visited = set()
        curr = 0
        new_curr = 0
        maxi = 0
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    curr = 1
                    q = deque([(i,j)])
                    while q:
                        r,c = q.popleft()
                        for dr,dc in dirs:
                            nr = dr + r
                            nc = dc + c
                            if 0<=nr < rows and 0<=nc < col and (nr,nc)not in visited and grid[nr][nc]==1:
                                visited.add((nr,nc))
                                curr = curr + 1
                                q.append((nr,nc))
                    maxi = max(maxi,curr)
        return maxi 


