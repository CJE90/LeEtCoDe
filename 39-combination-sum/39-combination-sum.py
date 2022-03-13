class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def explore(index, path, target):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return 
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                target -= candidates[i]
                if target >= 0:
                    explore(i, path, target)
                target += candidates[i]
                path.pop()
        
        explore(0, [], target)
        return result