class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        ans = []

        def bfs(val):
            dq = deque([val])
            visited = set()
            visited.add(val)

            artic = pacific = False
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while dq:
                r, c = dq.popleft()
                val = heights[r][c]
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c

                    if (nr < 0 or nc < 0):
                        pacific = True
                        continue
                    
                    if (nr >= row or nc >= col):
                        artic = True
                        continue
                    
                    if heights[nr][nc] > val: 
                        continue
                    if (nr, nc) in visited:
                        continue
                    

                    dq.append((nr, nc))
                    visited.add((nr, nc))

            return [artic, pacific]

        for r in range(row):
            for c in range(col):
                l = bfs((r, c))
                if l[0] == l[1] == True:
                    ans.append([r,c])
        return (ans)