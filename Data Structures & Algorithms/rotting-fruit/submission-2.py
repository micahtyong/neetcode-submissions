from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lst = deque()
        num_fresh_fruit = 0

        # Find current set of rotten fruit.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    lst.append((i, j, 0)) # minute: 0
                elif grid[i][j] == 1:
                    num_fresh_fruit += 1
        # print(lst, num_fresh_fruit)

        def in_bounds(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        # Run BFS.
        time_elapsed = 0
        while len(lst) > 0:
            i, j, minute = lst.popleft()
            time_elapsed = max(time_elapsed, minute)
            neighbors = [
                (i + 1, j), # up
                (i - 1, j), # down
                (i, j + 1), # right
                (i, j - 1)  # left
            ]
            for x, y in neighbors:
                if in_bounds(x, y) and grid[x][y] == 1:
                    grid[x][y] = 2 # mark as newly rotten
                    num_fresh_fruit -= 1
                    lst.append((x, y, minute + 1))

        # Finally, check if all fruits were spoiled.
        if num_fresh_fruit > 0:
            return -1

        return time_elapsed