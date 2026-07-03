class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()

        def dfs(r, c, ind):
            if ind == len(word):
                return True
            
            if (r < 0 or r >= row or
                c < 0 or c >= col or 
                board[r][c] != word[ind] or
                (r, c) in visited
                ):

                return False

            visited.add((r, c))
            
            res = ( dfs(r + 1, c, ind + 1) or
                    dfs(r - 1, c, ind + 1) or 
                    dfs(r, c + 1, ind + 1) or
                    dfs(r, c - 1, ind + 1)
                    )
            
            visited.remove((r,c)) # Backtracking
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        
        return False