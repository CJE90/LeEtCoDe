class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ans = []
        for i in range(len(nums1)):
            val = d.get(nums1[i])
            if val == None:
                d[nums1[i]] = 1
            else:
                d[nums1[i]] = d.get(nums1[i])+1
        for i in range(len(nums2)):
            if d.get(nums2[i]) != None:
                ans.append(nums2[i])
                if d.get(nums2[i])-1 == 0:
                    del d[nums2[i]]
                else:
                    d[nums2[i]] = d.get(nums2[i])-1
        return ans
        