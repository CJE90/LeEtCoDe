class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)
        visited = set()
        for course, pre_req in prerequisites:
            adj_list[pre_req].append(course)
            
        def cycle(node, tracker, visited):
            if node in visited:
                return False
            tracker[node] = True
            for n in adj_list[node]:
                if n in tracker or cycle(n, tracker, visited):
                    return True
            del tracker[node]
            visited.add(node)
            return False
           
        
        for i in range(numCourses):
            tracker = {}
            if cycle(i, tracker, visited):
                return False
        return True
        