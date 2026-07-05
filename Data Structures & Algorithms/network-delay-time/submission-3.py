from heapq import heappush, heapify, heappop
from collections import defaultdict

# Feedback to self
# - Try modifying values a bit and see what the solution looks like
# ex) For example 1, what if we had [1, 2, 3] as the first edge? Then cost = 4. 
# - Try writing out example cases that would fail graphically


class Solution:
    # Actually, this was not far off from the most optimal solution!
    # We basically did Dikstra's. Here are a few improvements to make:
    # - Heap is just (time, sourceNode). 
    # - Initialize it to (0, k)
    # - Check visited list before adding  
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # BFS generally used to find shortest path.
        # In this problem, we need the cheapest path that hits all nodes.
        # At a given node, you can visit any of its neighbors and go down that route.
        # We can try a greedy solution where we always choose to send a signal
        # to the cheapest node. 

        # NOTE: You can explore from the same node IN PARALLEL!
        # Or to have a list the represents "time since visit"
        # [0 for i in range n]
        # Increment at every turn if we visited
        time = 0
        visited = set([k])

        # To represent the graph, let's just create a hashmap where the key is
        # the starting node, and the values are the directed edges + cost.
        # We can do some pre-processing here s.t. cost is the first element 
        # in the tuple.
        graph = defaultdict(list)
        for [ui, vi, ti] in times:
            graph[ui].append((ti, ui, vi)) # (cost, ui, vi)
        # print("directed graph", graph)

        # We'll use a PQ to represent the edge to explore next. 
        # We will keep track of the cost. 
        # We will keep track of nodes visited via set.
        # If we already visited the node, we should pop off from the stack 
        # and not consider it.
        to_explore = graph[k]
        heapify(to_explore)
        # print("starting edges to explore", to_explore, "at k =", k)
        while len(to_explore) > 0:
            ti, ui, vi = heappop(to_explore)
            # print("exploring directed edge from", ui, "to", vi, "at time", ti, "where currtime is", time)
            # Already found a cheaper way to visit this node. 
            # This is also how we handle cycle detection
            if vi in visited:
                # print("already seen", vi)
                continue
            # Exploring!
            visited.add(vi)
            time = ti # Fast forward to new time
            for [new_ti, new_ui, new_vi] in graph[vi]:
                # time to dequeue!
                new_time = new_ti + time
                heappush(to_explore, (new_time, new_ui, new_vi))
            # print("heap edges to explore now looks like", to_explore, "and new time is", time)
            
        # For example 1, we start at k = 1.
        # We can put (1, 2, 1) and (1, 4, 4) into our min heap. 
        # Since (1, 2, 1) has the cheapest cost, we pop that edge from the heap.
        # We see that node 2 has not been explored, so we explore it. 
        # We increment cost by 1. 
        # We add (2, 3, 1) to the heap.
        # Since (2, 3, 1) has the cheapest cost, we pop that edge from the heap.
        # ...
        # Until we get to 4. At this point, we see that all nodes have been visited!
        # We can return the cost without needing to explore further.

        # If there are no more edges to explore in the PQ, 
        # but not all nodes have been visited, return -1
        if len(visited) < n:
            # print("visited does not include all n", visited, n)
            return -1

        return time










