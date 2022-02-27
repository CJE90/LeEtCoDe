class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        valid = True
        for word in words:
            valid = True
            if len(word) < len(pref):
                continue
            for i,c in enumerate(pref):
                if c != word[i]:
                    valid = False
                    break
            if valid:
                count += 1
        return count
        