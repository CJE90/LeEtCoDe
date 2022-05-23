class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mag_lookup = Counter(magazine)
        for c in ransomNote:
            if c not in mag_lookup:
                return False
            mag_lookup[c] -= 1
            if mag_lookup[c] < 1:
                del mag_lookup[c]
        return True