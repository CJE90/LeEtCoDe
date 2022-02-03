class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        Ht = Counter(nums)
        
        for keys in Ht:
            if k > 0 and keys+k in Ht:
                result += 1
            elif k == 0 and Ht[keys] > 1:
                result +=1
        return result
        
        