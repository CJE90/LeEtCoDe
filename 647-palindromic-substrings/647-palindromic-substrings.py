class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            count += self.count_around_center(s, i, i)
            count += self.count_around_center(s, i, i+1)
        return count
    
    
    def count_around_center(self, s: str, lo: int, hi: int) -> int:
        result = 0
        while lo >= 0 and hi < len(s):
            if s[lo] != s[hi]:
                break
            lo -= 1
            hi += 1
            result +=1
        return result