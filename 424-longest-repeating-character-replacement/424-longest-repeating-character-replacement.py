class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        #track frequency of chars
        #violated when # of distinct chars exceed k
        #K can be 0
        #length of window - most frequent char > k: shrink the window
        l = 0
        seen = defaultdict(int)
        longestFound = 0
        
        for r in range(len(s)):
            seen[s[r]] += 1
            mostFrequent = max(seen.values())
            while r-l+1 - mostFrequent > k:
                seen[s[l]] -= 1
                if seen[s[l]] < 1:
                    seen.pop(s[l])
                l+=1
                mostFrequent = max(seen.values())
            longestFound = max(longestFound, r-l+1)
        return longestFound
            
        