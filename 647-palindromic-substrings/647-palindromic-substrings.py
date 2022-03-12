class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        k = 1
        
        def isPalindrom(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrom(s, i, j):
                    count += 1
        return count
                
        