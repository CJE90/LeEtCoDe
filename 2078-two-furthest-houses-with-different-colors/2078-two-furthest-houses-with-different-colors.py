class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, len(colors)-1
        maxFound = -1
        color1, color2 = colors[l], colors[r]
        for index, color in enumerate(colors):
            if color != color1:
                if index > maxFound:
                    maxFound = index
            if color != color2:
                if len(colors)-1-index > maxFound:
                    maxFound = len(colors)-1-index
        return maxFound
                
            
        
        
        