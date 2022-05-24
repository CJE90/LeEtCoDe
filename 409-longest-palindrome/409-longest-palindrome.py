class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        letters = set()
        for c in s:
            if c in letters:
                count += 2
                letters.remove(c)
            else:
                letters.add(c)
        return count if len(letters) == 0 else count+1
        