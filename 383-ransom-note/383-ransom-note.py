class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_lookup = Counter(ransomNote)
        mag_lookup = Counter(magazine)
        for c in note_lookup:
            while note_lookup[c] > 0:
                if c not in mag_lookup:
                    return False
                mag_lookup[c] -= 1
                if mag_lookup[c] == 0:
                    del mag_lookup[c]
                note_lookup[c] -= 1
        return True