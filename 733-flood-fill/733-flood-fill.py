class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or image[sr][sc] == newColor:
            return image
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        self.dfs(image, sr, sc, newColor, oldColor)
        return image
    
    def dfs(self, image, sr, sc, newColor, oldColor):
        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx = sr+dx
            ny = sc+dy
            if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == oldColor:
                image[nx][ny] = newColor
                self.dfs(image, nx, ny, newColor, oldColor)
            
    