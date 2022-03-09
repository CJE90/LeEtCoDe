class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        subset = []
        lookup = defaultdict(list)
        
        def dfs(i):
            if i >= len(nums):
                if tuple(subset) not in lookup:
                    result.append(subset.copy())
                    lookup[tuple(subset)] = 1
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return result
        