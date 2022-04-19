class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        buckets = [0]*26
        for c in s:
            buckets[ord(c)%ord('a')] += 1
        for c in t:
            buckets[ord(c)%ord('a')] -= 1
        for b in buckets:
            if b != 0:
                return False
        return True
       
    