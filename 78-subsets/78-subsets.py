class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def explore(index, path):
            result.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                explore(i+1, path)
                path.pop()
        explore(0,[])
        return result