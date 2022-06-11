class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key = lambda x: self.distance(x))
        return points[0:k]
        
    def distance(self, point):
        return sqrt(point[0]*point[0]+point[1]*point[1])
        