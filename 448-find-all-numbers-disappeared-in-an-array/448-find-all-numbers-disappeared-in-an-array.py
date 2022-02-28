class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0 for val in nums]
        result = []
        for val in nums:
            arr[val-1] = 1
        for i in range(len(arr)):
            if arr[i] != 1:
                result.append(i+1)
        return result
        