# Naive
# Set of servers that communicate with at least one other server (xy coordinates)
# Count # of servers on a row. If > 1, add all of those to the set
# Count # of servers on a col. If > 1, add all of those to the col
# Runtime: O(mn). Space: O(mn)

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return False
        
        s = set()

        # Row connections
        for i in range(len(grid)):
            potential_set = set()
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    potential_set.add((i, j))
            if len(potential_set) > 1:
                s = s | potential_set 

        # Col connections
        for j in range(len(grid[0])):
            potential_set = set()
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    potential_set.add((i, j))
            if len(potential_set) > 1:
                s = s | potential_set
        
        # print(s)
        return len(s)