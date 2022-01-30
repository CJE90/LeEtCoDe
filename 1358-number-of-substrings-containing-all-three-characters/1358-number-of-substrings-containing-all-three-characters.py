class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        lookup = defaultdict(int)
        count = 0
        
        for r in range(len(s)):
            lookup[s[r]] += 1
            
            while len(lookup) == 3:
                count += len(s)-r
                lookup[s[l]] -= 1
                if lookup[s[l]] < 1:
                    lookup.pop(s[l])
                l+=1
        return count
        