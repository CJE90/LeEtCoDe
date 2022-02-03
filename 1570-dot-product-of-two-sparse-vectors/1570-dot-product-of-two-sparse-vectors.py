class SparseVector:
    def __init__(self, nums: List[int]):
        self.ht = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] != 0:
                self.ht[i] = nums[i]
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for k, v in enumerate(self.ht):
            if v in vec.ht:
                result += self.ht[v] * vec.ht[v]
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

