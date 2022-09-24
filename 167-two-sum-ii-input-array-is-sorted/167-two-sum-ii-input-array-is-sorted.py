class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                return [left+1, right+1]
            elif _sum < target:
                left += 1
            else:
                right -= 1
        return []
        