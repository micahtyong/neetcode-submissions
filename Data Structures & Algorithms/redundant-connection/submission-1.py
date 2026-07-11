from collections import defaultdict 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Assumptions:
        # - If we can identify nodes in the cycle, we can simply return an edge from that cycle.
        # - There is only one cycle in each input.
        
        # DFS with backtracking to find nodes participating in the cycle
        # Exclude prefix that's not part of the cycle

        # Union find
        # Union the set and return node where we detected cycle 
        # Then recursion returns
        n = len(edges)

        # Make a graph from edges
        graph = defaultdict(list)
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Set for each node, will merge to find the connected component (cycle)
        # Edge to remove
        components = { key: (set([key]), set()) for key in range(1, n+1) }

        def dfs(k: int, prev: int, visited: set) -> int:
            """
            Return node number of the cycle we just hit.
            Return -1 if we've hit a leaf (e.g., no cycle)
            """
            if graph[k] == 1 and graph[k][0] == prev:
                return -1

            visited.add(k)
            for neighbor in graph[k]:
                edge = sorted([k, neighbor])
                if neighbor in visited and neighbor != prev:
                    # Cycle!
                    print(f"We found a cycle with {k} and {neighbor}")
                    components[neighbor][0].add(k)
                    components[neighbor][1].add(tuple(edge))
                    return neighbor
                elif neighbor not in visited:
                    val = dfs(neighbor, k, visited)
                    # Close the cycle
                    if val == k:
                        return -1 
                    elif val > -1:
                        print(f"They found a cycle! I'm node {k}. Merging and backtracking..")
                        components[val][0].add(k)
                        components[val][1].add(tuple(edge))
                        return val
            return -1

        # Start at 1 (but can be any node), run DFS w/ backtracking
        print(f"components before {components}")
        dfs(1, -1, set())
        print(f"components after {components}")
        
        # Components should contain the cycle
        for _, v in components.items():
            _, edges_in_cycle = v
            if len(edges_in_cycle) > 1:
                for edge in edges[::-1]:
                    edge = tuple(edge)
                    if edge in edges_in_cycle:
                        return list(edge)
        return []
                