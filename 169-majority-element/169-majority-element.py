class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        answer = None
        
        for num in nums:
            if count == 0:
                answer = num
            if num == answer:
                count += 1
            else:
                count -= 1
        return answer
       
        
        