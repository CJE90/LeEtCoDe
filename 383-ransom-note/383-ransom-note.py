class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        note_lookup = Counter(ransomNote)
        mag_lookup = Counter(magazine)
        for char, count in note_lookup.items():
            if count > mag_lookup[char]:
                return False
        return True
        