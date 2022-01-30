class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = collections.Counter({0:1})
        result = 0
        runsum = 0
        
        for i in nums:
            runsum += i
            result += counter[runsum-goal]
            counter[runsum] += 1
        return result
       