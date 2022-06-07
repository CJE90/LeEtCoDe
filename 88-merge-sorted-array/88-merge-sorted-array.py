class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        copy = nums1[:m]
        p1 = 0
        p2 = 0
        for i in range(n+m):
            if p2 >= n or (p1 < m and copy[p1] <= nums2[p2]):
                nums1[i] = copy[p1]
                p1+=1
            else:
                nums1[i] = nums2[p2]
                p2+=1
                

        
        
        