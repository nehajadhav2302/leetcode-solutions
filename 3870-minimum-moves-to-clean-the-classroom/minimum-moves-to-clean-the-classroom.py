from collections import deque
from typing import List


class Solution:

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litters = []
        start_pos = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start_pos = (r, c)
                elif classroom[r][c] == "L":
                    litters.append((r, c))

        num_litter = len(litters)
        full_mask = (1 << num_litter) - 1

        litter_map = {pos: i for i, pos in enumerate(litters)}

        # best_energy[r][c][mask] stores maximum remaining energy for state (r, c, mask)
        best_energy = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]

        sr, sc = start_pos
        initial_mask = 0
        if (sr, sc) in litter_map:
            initial_mask |= 1 << litter_map[(sr, sc)]

        if initial_mask == full_mask:
            return 0

        queue = deque([(sr, sc, initial_mask, energy, 0)])
        best_energy[sr][sc][initial_mask] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, steps = queue.popleft()

            # If we've reached full mask, return current steps
            if mask == full_mask:
                return steps

            # Skip if we already reached this state with strictly more energy
            if e < best_energy[r][c][mask]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                    next_e = e - 1

                    if next_e < 0:
                        continue

                    cell = classroom[nr][nc]

                    # Reset energy if cell is 'R'
                    if cell == "R":
                        next_e = energy

                    next_mask = mask
                    if (nr, nc) in litter_map:
                        next_mask |= 1 << litter_map[(nr, nc)]

                    if next_e > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))

        return -1