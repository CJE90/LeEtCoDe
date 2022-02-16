class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        def dfs(room):
            for keys in rooms[room]:
                if keys not in visited:
                    visited.add(keys)
                    dfs(keys)
        dfs(0)
        return len(visited) == len(rooms)
    
    
