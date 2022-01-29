class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        lookup = defaultdict(int)
        result = 0
        
        for r in range(len(s)):
            lookup[s[r]] += 1
            while len(lookup) == 3:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    lookup.pop(s[l])
                l+=1
            result +=l
        return result
            
        
        
        