from collections import deque

class Solution:
    def minMoves(self, classroom: list[list[str]], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sr = sc = -1
        litter_id = [[-1] * n for _ in range(m)]
        litter_count = 0

        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    sr, sc = r, c
                elif cell == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1
        best = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        
        q = deque([(sr, sc, 0, energy, 0)])
        best[sr][sc][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, mask, en, dist = q.popleft()

            if mask == full_mask:
                return dist

            if en == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X':
                    continue

                new_mask = mask
                if classroom[nr][nc] == 'L':
                    new_mask |= (1 << litter_id[nr][nc])

                new_en = energy if classroom[nr][nc] == 'R' else en - 1

                if best[nr][nc][new_mask] < new_en:
                    best[nr][nc][new_mask] = new_en
                    q.append((nr, nc, new_mask, new_en, dist + 1))

        return -1