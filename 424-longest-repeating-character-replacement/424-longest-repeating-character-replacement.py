class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longestFound = 0
        count = defaultdict(int)
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]]+=1
            if count[s[r]] > maxf:
                maxf = count[s[r]]
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+=1
            longestFound = max(longestFound, r-l+1)
        return longestFound
    

        
            
            
    
                            
                
            