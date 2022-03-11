class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        result = []
        visited = set()
        heapq.heappush(minHeap, (nums1[0]+nums2[0], 0 , 0))
        visited.add((0,0))
        while k > 0 and minHeap:
            smallSum, i, j = heapq.heappop(minHeap)
            result.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1,j) not in visited:
                heapq.heappush(minHeap, (nums1[i+1]+nums2[j], i+1 , j))
                visited.add((i+1,j))
            if j+1 < len(nums2) and (i,j+1) not in visited:
                heapq.heappush(minHeap, (nums1[i]+nums2[j+1], i , j+1))
                visited.add((i,j+1))
            k -= 1
        return result
            
        
        















































#         minHeap = []
#         visited = set()
#         result = []
        
#         heapq.heappush(minHeap, (nums1[0]+nums2[0], 0, 0))
#         visited.add((0,0))
        
#         while minHeap and len(result) < k:
#             pairSum, i, j = heapq.heappop(minHeap)
#             result.append([nums1[i],nums2[j]])
            
#             if i+1 < len(nums1) and (i+1, j) not in visited:
#                 heapq.heappush(minHeap, (nums1[i+1]+nums2[j], i+1, j))
#                 visited.add((i+1,j))
            
#             if j+1 < len(nums2) and (i, j+1) not in visited:
#                 heapq.heappush(minHeap, (nums1[i]+nums2[j+1], i, j+1))
#                 visited.add((i,j+1))
#         return result
                
        
#         '''
#         1 2 11
#         2 4 6 
        
#         [1,2], [1,4] [1,6]
#         (sumofPair, i, j)
#         1. put first pair in minHeap
#         2. pop first element and add next increment from each array into min heap 
#             i. i+1,j    i, j+1
#             0,0 1,0 0,1 
#         3.  keep visited set
#         '''
        