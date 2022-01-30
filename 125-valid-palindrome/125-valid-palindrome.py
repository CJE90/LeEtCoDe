class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = filter(lambda x:x.isalnum(),s)
        res = list(s2)
        l = 0
        r = len(res)-1
        
        while l < r:
            if res[l].isalpha() and res[r].isalpha():
                if res[l].lower() != res[r].lower():
                    return False
            elif res[l] != res[r]:
                return False
            
            l+= 1
            r-=1
        return True
        