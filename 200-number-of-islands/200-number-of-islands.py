class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        count = 0
        def bfs(r,c):
            visited.add((r,c))
            que = deque([(r,c)])
            while que:
                row,col = que.popleft()
                for newRow, newCol in ((row+1,col),(row-1,col),(row,col-1),(row,col+1)):
                    if 0 <= newRow < m and 0 <= newCol < n and (newRow,newCol) not in visited and grid[newRow][newCol] == "1":
                        que.append((newRow,newCol))
                        visited.add((newRow,newCol))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    count += 1
        return count
        