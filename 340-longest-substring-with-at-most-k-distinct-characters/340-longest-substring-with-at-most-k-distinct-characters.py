class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k is 0:
            return 0
        seen = defaultdict(int)
        l = 0
        longestFound = -inf
        
        for r in range(len(s)):
            seen[s[r]] += 1
            while len(seen) > k and l<r:
                seen[s[l]]-=1
                if seen[s[l]] < 1:
                    seen.pop(s[l])
                l+=1
            longestFound = max(longestFound, r-l+1)
        return longestFound
                
        