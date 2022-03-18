class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix = []
        runSum = 0
        
        for i,v in enumerate(nums):
            runSum += v
            prefix.append(runSum)
        ma = prefix[k-1]
        for i in range(k,len(prefix)):
            ma = max(ma, prefix[i]-prefix[i-k])
        return ma /k
            
            
            
        