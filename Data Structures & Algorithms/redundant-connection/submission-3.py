from collections import defaultdict 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.findRedundantConnectionUnionFind(edges)
        # return findRedundantConnectionTopo(edges)
        # return findRedundantConnectionDFS(edges)
    
    def findRedundantConnectionUnionFind(self, edges: List[List[int]]) -> List[int]:
        # Union find with path compression
        # Each node is its own component

        # Process each edge and union them
        n = len(edges)
        # Each node starts off as its own parent
        nodeParentMap = { k: k for k in range(1, n + 1) }
        print(f"Starting node parent map {nodeParentMap}")
        
        def findParent(k: int) -> int:
            # Path compression should happen in here
            if nodeParentMap[k] == k:
                return k
            
            parent = findParent(nodeParentMap[k])
            # print(f"parent of k {k} is {parent}")
            nodeParentMap[k] = parent # path compression
            return parent
            
        def union(a: int, b: int) -> None:
            parentA, parentB = findParent(a), findParent(b)
            nodeParentMap[parentA] = parentB

        for [a, b] in edges:
            # Already connected! This is the first edge that produces a cycle.
            if findParent(a) == findParent(b):
                return [a, b]
            else:
                union(a, b)
                print(f"node parent map {nodeParentMap} after unioning {a} and {b}")
            
        
    
    # More performant than DFS soln empirically; clean
    def findRedundantConnectionTopo(self, edges: List[List[int]]) -> List[int]:
        # Kahn's algorithm
        # Start with nodes of indegree of 1 (leaves)
        # Pop off the graph
        # If no more leaves found but we still have a graph, we have our cycle
        # Return one edge in there
        graph = defaultdict(set)
        for [a, b] in edges:
            graph[a].add(b)
            graph[b].add(a)
        print(f"Starting graph: {graph}")
        
        leaves = [k for k in graph.keys() if len(graph[k]) == 1]
        print(f"Starting set of leaves {leaves}")
        while len(leaves) > 0:
            new_leaves = []
            for leaf in leaves:
                branch = graph[leaf].pop()
                graph[branch].remove(leaf)
                del graph[leaf]
                if len(graph[branch]) == 1: new_leaves.append(branch)
            leaves = new_leaves
            print(f"After one iteration, resulting set of leaves {leaves}")
        
        print(f"Resulting cycle graph: {graph}")
        for [a, b] in reversed(edges):
            if a in graph and b in graph and b in graph[a]:
                return [a, b]
        


    def findRedundantConnectionDFS(self, edges: List[List[int]]) -> List[int]:
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
                