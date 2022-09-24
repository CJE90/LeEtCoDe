class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # X + Y + Z == 0
        # Y + Z = -X
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.search_for_trips(nums, -nums[i], i+1, result)
        return result
    def search_for_trips(self, arr, target_sum, left, result):
        right = len(arr)-1
        while left < right:
            _sum = arr[left]+arr[right]
            if _sum == target_sum:
                result.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:                    
                        left += 1
                while left < right and arr[right] == arr[right+1]:
                        right -= 1
            elif _sum < target_sum:
                left += 1
            else:
                right -= 1
        
                
        