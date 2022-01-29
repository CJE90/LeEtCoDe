class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longestFound = 0
        lookup = defaultdict(int)
        
        for r in range(len(s)):
            lookup[s[r]] += 1
            
            while lookup[s[r]] > 1:
                lookup[s[l]] -= 1
                if lookup[s[l]] < 1:
                    lookup.pop(s[l])
                l+=1
            
            longestFound = max(longestFound, r-l+1)
            
        return longestFound
        