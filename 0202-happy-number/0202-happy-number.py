class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.getSum(n)
        fast = self.getSum(self.getSum(n))
        if slow == fast:
            return True
        while slow != fast:
            slow = self.getSum(slow)
            fast = self.getSum(self.getSum(fast))
            if fast == 1:
                return True
        return False
        
    def getSum(self, n):
        _sum = 0
        while n >= 10:
            digit = n % 10
            _sum += digit**2
            n = n // 10
        _sum += n**2
        return _sum
            
        