class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        maxFruit = 0
        holding = defaultdict(int)
        
        for r in range(len(fruits)):
            holding[fruits[r]] += 1
            
            while len(holding) > 2:
                holding[fruits[l]] -= 1
                if holding[fruits[l]] < 1:
                    holding.pop(fruits[l])
                l+=1
            
            maxFruit = max(maxFruit, r-l+1)
        return maxFruit
        