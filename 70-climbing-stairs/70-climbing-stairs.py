class Solution:
    def climbStairs(self, n: int) -> int:
        hashTable = {}
        def dfs(n):
            if n <= 2:
                hashTable[n] = n
                return hashTable[n]
            if n in hashTable:
                return hashTable[n]
            
            
            hashTable[n] = dfs(n-1)+dfs(n-2)
            return hashTable[n]
            
            
        
        return dfs(n)
        