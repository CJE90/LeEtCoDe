class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.search_pairs(nums, target, i , j, result)
        return result
    def search_pairs(self, nums, target, first, second, result):
        left = second + 1
        right = len(nums)-1
        while left< right:
            quad_sum = nums[first] + nums[second] + nums[left] + nums[right]
            if quad_sum == target:
                result.append([nums[first], nums[second], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif quad_sum < target:
                left +=1
            else:
                right -= 1
                    