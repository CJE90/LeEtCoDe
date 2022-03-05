class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        old, m, n = image[sr][sc], len(image), len(image[0])
        q = deque([(sr,sc)])
        while q:
            i,j = q.popleft()
            image[i][j] = newColor
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n and image[x][y] == old:
                    q.append((x,y))
        return image
    