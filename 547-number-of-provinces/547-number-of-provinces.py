class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        Uf = UnionByRank(len(isConnected))
        for city in isConnected:
            for i in range(len(city)-1):
                for j in range(i+1,len(city)):
                    if city[i] == 1 and city[j] == 1:
                        Uf.union(i, j)
        print(Uf.root)                
        #return len(Counter(Uf.root))
        return len(set([Uf.find(i) for i in range(len(isConnected))]))
            
           
        
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