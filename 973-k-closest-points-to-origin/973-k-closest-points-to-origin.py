class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        points.sort(key=lambda x: math.sqrt(x[0]*x[0] + x[1]*x[1]))
        #arr = sorted(points,key=lambda x: math.sqrt(x[0]*x[0] + x[1]*x[1]))
        for i, p in enumerate(points):
            if i>k-1:
                return res
            res.append(p)
    
        return res
        
        