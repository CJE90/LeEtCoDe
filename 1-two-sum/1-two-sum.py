class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        result = []
        for index,value in enumerate(nums):
            if value in lookup:
                result.append(lookup[value])
                result.append(index)
                return result
            lookup[target-value] = index
        return []
        