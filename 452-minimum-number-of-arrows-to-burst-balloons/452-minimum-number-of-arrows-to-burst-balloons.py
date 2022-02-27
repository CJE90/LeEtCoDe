class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        
        count = len(points)
        prevEnd = -inf
        for s,e in points:
            if s > prevEnd:
                prevEnd = e
                
            else:
                count -= 1
                
        return count
            
        