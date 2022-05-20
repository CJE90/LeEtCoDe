class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup1 = Counter(s)
        lookup2 = Counter(t)
        return lookup1 == lookup2
        