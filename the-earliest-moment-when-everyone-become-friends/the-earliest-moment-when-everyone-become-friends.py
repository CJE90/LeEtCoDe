class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])

        UF = UnionByRank(n)
        for meeting in logs:
            UF.union(meeting[1], meeting[2])
            if UF.n == 1:
                return meeting[0]
        return -1
        
        
        
class UnionByRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.n = size
    
    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.n -= 1
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        
        