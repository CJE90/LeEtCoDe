class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = 0 
        d = defaultdict(int)

        for r in range(len(s)):
            d[s[r]]+=1

            while len(d) == 3:
                count += len(s)-r
                d[s[l]] -= 1
                if d[s[l]] < 1:
                    d.pop(s[l])
                l += 1
      
        return count
            
        
        
        