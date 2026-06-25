class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        visited = set()
        history = []
        
        for i in range(n):
            state_tuple = tuple(cells)
            
            if state_tuple in visited:
                cycle_start = history.index(state_tuple)
                cycle_length = i - cycle_start
                remaining_days = (n - i) % cycle_length
                return self.prisonAfterNDays(cells, remaining_days)
            
            visited.add(state_tuple)
            history.append(state_tuple)
            
            x = [0] * 8
            for j in range(1, 7):
                if cells[j-1] == cells[j+1]:
                    x[j] = 1
                else:
                    x[j] = 0
            cells = x
            
        return cells