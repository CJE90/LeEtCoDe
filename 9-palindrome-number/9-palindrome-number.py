class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        if x < 0:
            return False
        while x > 0:
            l.append(x%10)
            x = x//10
        return self.determine_palindrome(l)
    def determine_palindrome(self, li):
        l = 0
        r = len(li)-1
        while l<r:
            if li[l] != li[r]:
                return False
            l+=1
            r-=1
        return True
        