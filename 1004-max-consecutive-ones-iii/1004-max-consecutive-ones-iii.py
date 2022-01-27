class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        longestFound = -inf
        
        for r in range(len(nums)):
            if nums[r] is 0:
                k-=1
            while k < 0 and l<=r:
                if nums[l] is 0:
                    k+=1
                l+=1
            longestFound = max(longestFound, r-l+1)
        return longestFound
                
        