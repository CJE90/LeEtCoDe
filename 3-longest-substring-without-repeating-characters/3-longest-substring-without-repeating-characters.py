class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, n = 0, 0, len(s)
        longestFound = -inf
        if n is 0:
            return 0
        seen = defaultdict(int)
        
        for r in range(len(s)):
            while s[r] in seen and l<=r:
                seen[s[l]] -= 1
                if seen[s[l]] < 1:
                    seen.pop(s[l])
                l+=1
               
            seen[s[r]] += 1
            longestFound = max(longestFound,r-l+1)
        return longestFound
                
            
                    
            
        
        