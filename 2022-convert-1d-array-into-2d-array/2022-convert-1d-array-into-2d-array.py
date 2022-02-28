class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(m)]
        N = len(original)
        if N != m*n:
            return []
        for i in range(N):
            result[i//n][i%n] = original[i]
        return result
        