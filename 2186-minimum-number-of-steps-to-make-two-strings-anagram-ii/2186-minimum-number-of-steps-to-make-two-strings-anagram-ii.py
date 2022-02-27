class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(t)> len(s):
            s,t = t,s
        lookup = Counter(s)
        for c in t:
            if c in lookup:
                lookup[c] -= 1
                if lookup[c] == 0:
                    lookup.pop(c)
            else:
                lookup[c] -= 1
        sum = 0
        for val in lookup.values():
            sum += abs(val)
        return sum
      
        