class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        
        def explore(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    explore(key)
        
        
        explore(0)
        return len(visited) == len(rooms)