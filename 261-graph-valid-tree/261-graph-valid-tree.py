class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = UnionByRank(n)
        for edge in edges:
            if UF.connected(edge[0], edge[1]):
                return False
            else:
                UF.union(edge[0], edge[1])
        a = set()
        for i in range(n):
            a.add(UF.find(i))
        
        return len(a) == 1
        
        
        
class UnionByRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
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
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        

        