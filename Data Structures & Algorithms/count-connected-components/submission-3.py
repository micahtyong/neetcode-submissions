# Union-find with path compression.
# Data structures
#   - num_connected initialized to n
#   - parents list initialized to [i for i in range(n)]
#   - [opt] size list initialized to [1 for each elem in edges]
# Helper methods
#   - find(x)
#       - find the root
#       - set any intermediaries to that root
#   - union(i,j)
#       - find roots of i and j
#       - if equal, return
#       - otherwise, set smaller root to parent
# For each union, if they are not already part of the same component, num_connected -= 1

# Edge cases
#   - Cycles: Won't be represented as a cycle in our data struct.
#       - Split happens and edges go to the parent representative

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_connected = n
        parent = [i for i in range(n)]
        sizes = [1 for _ in range(n)]
        
        def find(x) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def find_iter(x) -> int: 
            # Find root
            root = x
            while parent[root] != root:
                root = parent[root]
             
            # Path compression
            ptr = x
            while parent[ptr] != root:
                temp = ptr
                ptr = parent[ptr]
                parent[temp] = root

            return root

        def union(i, j) -> None:
            nonlocal num_connected
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j: return
            
            # TODO: Size optimization
            if sizes[root_i] >= sizes[root_j]:
                parent[root_j] = root_i
                sizes[root_j] += sizes[root_i]
            else:
                parent[root_i] = root_j
                sizes[root_i] += sizes[root_j]
            num_connected -= 1


        for edge in edges:
            i, j = edge
            union(i, j)
            # print(parent, num_connected)

        return num_connected
        