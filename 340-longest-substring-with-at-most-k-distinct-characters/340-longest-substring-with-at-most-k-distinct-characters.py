class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lookup = defaultdict(int)
        l = 0
        
        maxWin = 0
        for r in range(len(s)):
            lookup[s[r]] += 1
            while len(lookup) > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] <= 0:
                    lookup.pop(s[l])
                l+=1
            
            if len(lookup) <= k:
                maxWin = max(maxWin, r-l+1)
        return maxWin
        