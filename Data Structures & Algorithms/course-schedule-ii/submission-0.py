from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algorithm.
        # 1. Build indegree list and graph.
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for prereq in prerequisites:
            course_a, course_b = prereq # B->A
            indegree[course_a] += 1
            graph[course_b].append(course_a)
        
        print("graph", graph, "indegree", indegree)
        # 2. Figure out all classes with degree 0.
        q = deque()
        for i, c in enumerate(indegree):
            if c == 0:
                q.append(i)
        print("starting list", q)
        # 3. Run topo sort, keep track of visited order.
        order = []
        while len(q) > 0:
            curr = q.popleft()
            order.append(curr) # Take the class
            for next_class in graph[curr]:
                indegree[next_class] -= 1
                if indegree[next_class] == 0:
                    q.append(next_class)
        
        print("order", order, "remaining indegree", indegree)
        if len(order) == numCourses:
            return order
        print("could not take all classes")
        return []