class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n
        inDegree = [0 for i in range(n)]
        outDegree = [0 for i in range(n)]
        for relationship in trust:
            
            inDegree[relationship[1]-1] += 1
            outDegree[relationship[0]-1] += 1
        
        print(inDegree)
        print(outDegree)
        for i in range(0,n):
            if inDegree[i] == n-1 and outDegree[i] == 0:
                return i+1
        return -1
        
        