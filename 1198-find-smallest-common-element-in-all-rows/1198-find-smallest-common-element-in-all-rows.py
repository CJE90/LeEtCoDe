class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        lookup = defaultdict(int)
        ans = inf
        for l in mat:
            for e in l:
                lookup[e] += 1        
        for k,v in lookup.items():
            if v == len(mat):
                ans = min(ans,k)
        return -1 if ans == inf else ans