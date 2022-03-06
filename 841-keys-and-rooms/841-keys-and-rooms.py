class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        visited = set()
        def exploreRooms(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    exploreRooms(key)
        exploreRooms(0)
        
        return len(rooms) == len(visited)
        