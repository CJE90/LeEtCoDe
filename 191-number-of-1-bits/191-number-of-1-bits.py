class Solution:
    def hammingWeight(self, n: int) -> int:
        v = str(bin(n))
        count = 0
        for c in v:
            if c == '1':
                count += 1
        return count