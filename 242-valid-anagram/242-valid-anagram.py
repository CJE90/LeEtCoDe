class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        lookup = defaultdict(int)
        for c in s:
            lookup[c] += 1
        for c in t:
            lookup[c] -=1
            if lookup[c] < 0:
                return False
        for item in lookup.values():
            if item < 0:
                return False
        return True