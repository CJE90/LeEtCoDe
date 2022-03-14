class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        
        def explore(room):
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    explore(key)
        
        
        explore(0)
        return len(visited) == len(rooms)
    
    
    
  