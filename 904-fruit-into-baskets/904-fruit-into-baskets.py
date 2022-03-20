class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lookup = defaultdict(int)
        l = 0
        maxWin = 0
        for r in range(len(fruits)):
            lookup[fruits[r]] += 1 
            
            if len(lookup) > 2:
                lookup[fruits[l]] -= 1
                if lookup[fruits[l]] == 0:
                    lookup.pop(fruits[l])
                l+=1
                
            
            maxWin = max(maxWin, r-l+1)
        return maxWin
        
        