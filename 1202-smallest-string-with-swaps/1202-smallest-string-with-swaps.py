class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        UF = UnionByRank(len(s))
        for x,y in pairs:
            UF.union(x,y)
        groups = defaultdict(list)
        #print(UF.root)
        for i in range(len(s)):
            groups[UF.find(i)].append(s[i])
        #print(groups)
        for keys in groups.keys():
            #print(keys)
            groups[keys].sort()
        #print(groups)
        
        res = []
        for i in range(len(s)):
            res.append(groups[UF.find(i)].pop(0))
        return "".join(res)
        
      
    
    
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
        