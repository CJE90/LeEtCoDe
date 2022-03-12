class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        
        for i in range(len(s)):
            result1 = self.exploreOut(s, i, i)
            result2 = self.exploreOut(s, i, i+1)
            
            if len(result1) > len(result):
                result = result1
            if len(result2) > len(result):
                result = result2
            
        return "".join(result)
    
    def exploreOut(self, s, lo, hi):
        result = []
        
        while lo >= 0 and hi < len(s):
            if s[lo] == s[hi]:
                result = s[lo:hi+1]
                l = hi-lo+1
                lo -= 1
                hi += 1
            else:
                break
        return result
            