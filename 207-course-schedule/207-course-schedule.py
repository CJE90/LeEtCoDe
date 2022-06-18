class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj_list = collections.defaultdict(list)
        for course, pre_req in prerequisites:
            adj_list[pre_req].append(course)
            
        def cycle(node, tracker, visited):
            visited.add(node)
            tracker[node] = True
            for n in adj_list[node]:
                if (n not in visited and cycle(n, tracker, visited)) or n in tracker:
                    return True
                # elif n in tracker:
                #     return True
            del tracker[node]
            
            return False
           
        
        for i in range(numCourses):
            tracker = {}
            if i not in visited and cycle(i, tracker, visited):
                return False
        return True
        
#         adj_list = collections.defaultdict(list)
#         for course, pre_req in prerequisites:
#             adj_list[pre_req].append(course)
        
#         visited = []
#         visiting = set()
#         def explore(node):
#             if node in visiting:
#                 return False
#             visiting.add(node)
#             for n in adj_list[node]:
#                 if not explore(n):
#                     return False
#             visiting.remove(node)
#             visited.append(node)
#             adj_list[node] = []
#             return True
        
#         for n in range(numCourses):
#             if not explore(n):
#                 return False
#         print(visited)
#         return True
            

        