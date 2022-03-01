class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 1
        hi = max(nums)
        
        def goodCount(count):
            runsum = 0
            for val in nums:
                if val <= count:
                    runsum +=1
                
            return runsum > count
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if goodCount(mid):
                hi = mid
            else:
                lo = mid+1
        return lo
        
        
        