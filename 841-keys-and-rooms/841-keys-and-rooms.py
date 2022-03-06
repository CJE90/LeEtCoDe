class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        que = collections.deque()
        que.append(0)
        visited.add(0)
        
        while que:
            room = que.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    que.append(key)
        return len(rooms) == len(visited)
        
#         if not rooms:
#             return True
#         visited = set()
#         def exploreRooms(room):
#             visited.add(room)
#             for key in rooms[room]:
#                 if key not in visited:
#                     exploreRooms(key)
#         exploreRooms(0)
        
#         return len(rooms) == len(visited)
    #Time O(n): May need to explore each room
    #Space O(n): may need recursive stack call hold each room until the end
    
    
        