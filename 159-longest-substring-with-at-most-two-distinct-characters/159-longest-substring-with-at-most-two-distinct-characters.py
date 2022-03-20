class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lookup = defaultdict(int)
        l = 0
        maxWin = 0
        for r in range(len(s)):
            lookup[s[r]] += 1 
            
            if len(lookup) > 2:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    lookup.pop(s[l])
                l+=1
                
            
            maxWin = max(maxWin, r-l+1)
        return maxWin
        
        
        