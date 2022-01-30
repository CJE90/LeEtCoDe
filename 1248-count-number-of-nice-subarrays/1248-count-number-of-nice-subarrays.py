class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        ans = 0
        numOdd = 0
        
        for r in range(len(nums)):
            if nums[r] %2 != 0:
                numOdd += 1
                count = 0
            while l <= r and numOdd >= k:
                count += 1
                if nums[l] %2 != 0:
                    numOdd -= 1
                l+=1
            ans += count
        return ans