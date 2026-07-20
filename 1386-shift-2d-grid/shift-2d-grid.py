class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        newGrid = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                new_flat = (i * col + j + k) % (row * col)
                ni = new_flat // col
                nj = new_flat % col

                newGrid[ni][nj] = grid[i][j]

        return newGrid