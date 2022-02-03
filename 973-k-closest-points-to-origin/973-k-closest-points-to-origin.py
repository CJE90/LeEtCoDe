class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        arr = sorted(points,key=lambda x: math.sqrt(x[0]*x[0] + x[1]*x[1]))
        for i, p in enumerate(arr):
            if i>k-1:
                return res
            res.append(p)
    
        return res
        
        