class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)
        for course, pre_req in prerequisites:
            adj_list[pre_req].append(course)
        visited = set()
        visiting = set()
        def explore(node):
            if node in visiting:
                return False
            visiting.add(node)
            for n in adj_list[node]:
                if not explore(n):
                    return False
            visiting.remove(node)
            visited.add(node)
            adj_list[node] = []
            return True
        
        for n in range(numCourses):
            if not explore(n):
                return False
        return True
            
#         visited = set()
#         for course, pre_req in prerequisites:
#             adj_list[pre_req].append(course)
            
#         def cycle(node, tracker, visited):
#             visited.add(node)
#             tracker[node] = True
#             for n in adj_list[node]:
#                 if n not in visited and cycle(n, tracker, visited):
#                     return True
#                 elif n in tracker:
#                     return True
#             del tracker[node]
            
#             return False
           
        
#         for i in range(numCourses):
#             tracker = {}
#             if i not in visited and cycle(i, tracker, visited):
#                 return False
#         return True
        