# Naive
# Set of servers that communicate with at least one other server (xy coordinates)
# Count # of servers on a row. If > 1, add all of those to the set
# Count # of servers on a col. If > 1, add all of those to the col
# Runtime: O(mn). Space: O(mn)

# Improvements
# Perhaps we can iterate through the grid once?
# Dict for rows, dict for cols. Values are the subsets.
# At the end of the grid search, we perform union finds for any sets whose length is > 1
# Skips one double iter loop 

# row_count and col_count arrays
# loop through once, mark grid as visited as we go through
# for each element, if "1", we update row count and col count += 1 at pos
# after, we consolidate by iterating through, flipping to 0 for "faster" soln


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return False
        row_count = [0 for i in range(len(grid))]
        col_count = [0 for j in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # print("row_count", row_count, "col_count", col_count)
        res = 0
        for i, count in enumerate(row_count):
            if count > 1:
                # print("Row", i, "has at least 2 servers")
                for j in range(len(grid[0])):
                    # count and mark
                    if grid[i][j] == 1:
                        res += 1
                        grid[i][j] = "X" # mark as seen
        
        for j, count in enumerate(col_count):
            if count > 1:
                # print("Col", j, "has at least 2 servers")
                for i in range(len(grid)):
                    if grid[i][j] == 1:
                        res += 1
                        grid[i][j] = "X"
        
        # print(grid)
        return res
        


    def countServersNaive(self, grid: List[List[int]]) -> int:
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