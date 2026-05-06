class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row = len(boxGrid)
        col = len(boxGrid[0])

        rotated = []
        for i in range(col):
            rows = []
            for j in range(row):
                rows.append('.')
            rotated.append(rows)

        for r in range(row):
            
            count_stone = 0
            for c in range(col):
                if boxGrid[r][c] == '#':
                    count_stone += 1

                elif boxGrid[r][c] == '*':

                    new_r = c
                    new_c = row - 1 - r

                    rotated[new_r][new_c] = '*'
                    pos = c - 1

                    while count_stone > 0:
                        rotated[pos][new_c] = '#'
                        pos -= 1
                        count_stone -= 1
            place_row = col - 1
            while count_stone > 0:
                while rotated[place_row][row - 1 - r] == '*':
                    place_row -= 1

                rotated[place_row][row - 1 - r] = '#'

                place_row -= 1
                count_stone -= 1


        return rotated