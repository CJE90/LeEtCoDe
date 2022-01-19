class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        n = len(digits)
        for i in range(len(digits)):
            ans+=digits[i]*pow(10, n-1-i)
        return [int(x) for x in str(ans+1)]