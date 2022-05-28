class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        possible = None
        for n in nums:
            if count == 0:
                possible = n
            if n == possible:
                count +=1 
            else:
                count -= 1
        return possible
    
    