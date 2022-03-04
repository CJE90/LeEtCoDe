class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        lookup = Counter(t)
        need = len(t)
        
        l = 0
        minWindow = (0, len(s)+1)
        
        for r in range(len(s)):
            if s[r] in lookup:
                if lookup[s[r]] > 0:
                    need -= 1
                lookup[s[r]] -= 1
            
            while need == 0:
                if r -l < minWindow[1] - minWindow[0]:
                    minWindow = (l,r)
                if s[l] in lookup:
                    lookup[s[l]] += 1
                    if lookup[s[l]] > 0:
                        need +=1
                l+=1
        return s[minWindow[0]:minWindow[1]+1] if minWindow[1] - minWindow[0] < len(s) else ""
        
       