class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        
        l = 0
        lookup = Counter(s1)
        need = len(s1)
        
        
        for r in range(len(s2)):
            if s2[r] in lookup:
                
                if lookup[s2[r]] > 0:
                    need -= 1
                    
                lookup[s2[r]] -= 1
                
            if r-l+1 > len(s1):
                
                if s2[l] in lookup:
                    lookup[s2[l]] += 1
                    if lookup[s2[l]] > 0:
                        need += 1
                l+=1
                        
            
            if need == 0:
                return True
        return False
                
          
        