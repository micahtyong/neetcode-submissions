# BFS from each chest
# BFS > DFS for finding nearest; avoiding redundant work (e.g., cycles)
# Upper bound is O(kMN), where k is number of chests (can potentially be improved)
# Critical check is: If cell is visited and its value is <= counter, return early.

# Optimization: Multi-source BFS
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Find chests
        to_explore = deque()
        dist = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    to_explore.append((i, j, dist))
        
        # BFS for each chest
        def is_valid_to_explore(i, j) -> bool:
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] > 0

        # Opt: Multi-source BFS
        while len(to_explore) > 0:
            i, j, d = to_explore.popleft()
            
            neighbors = [
                (i + 1, j), # up
                (i - 1, j), # down
                (i, j + 1), # right
                (i, j - 1), # left
            ]
            for m, n in neighbors:
                if is_valid_to_explore(m, n) and d < grid[m][n]:
                    grid[m][n] = d
                    to_explore.append((m, n, d + 1))
        
        return