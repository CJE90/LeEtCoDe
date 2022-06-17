class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            
            while l<r:
                threeSum = nums[i]+nums[l]+nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    answer.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < len(nums) and nums[l] == nums [l-1]:
                        l+=1
        return answer