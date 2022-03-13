class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def explore(index, path, target):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                if (i > index and candidates[i] == candidates[i-1]) or candidates[i] > target:
                   
                    continue
                
                path.append(candidates[i])
                target -= candidates[i]
                explore(i+1, path, target)
                target += candidates[i]
                path.pop()
                        
        explore(0, [], target)
        return result
        
