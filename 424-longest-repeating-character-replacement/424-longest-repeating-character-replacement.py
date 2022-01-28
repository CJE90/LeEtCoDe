class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longestFound = 0
        count = defaultdict(int)
        
        for r in range(len(s)):
            largestCount = 0
            count[s[r]]+=1
            for val in count.values():
                largestCount = max(largestCount, val)
            while (r-l+1) - largestCount > k:
                count[s[l]] -= 1
                if count[s[l]]<1:
                    count.pop(s[l])
                l+=1
            longestFound = max(longestFound, r-l+1)
        return longestFound
            
            
    
                            
                
            