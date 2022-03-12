class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        max_val = -inf
        smallest_range = (-inf, inf)
        min_heap = []
         
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        while min_heap:
            val, i, j = heapq.heappop(min_heap)
            if max_val - val < smallest_range[1] - smallest_range[0]:
                smallest_range = (val, max_val)
            
            if j+1 < len(nums[i]):
                heapq.heappush(min_heap, (nums[i][j+1], i, j+1))
                max_val = max(max_val, nums[i][j+1])
            else:
                return [smallest_range[0], smallest_range[1]]
        
        return [smallest_range[0], smallest_range[1]]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         min_heap=[(List[0], index, 0) for index,List in enumerate(nums)]
#         heapq.heapify(min_heap)
#         max_val = max(l[0] for l in nums)
#         smallest_range = (-inf,inf)
#         while min_heap:
#             min_val, list_index, num_index = heapq.heappop(min_heap)
#             if max_val - min_val < smallest_range[1] - smallest_range[0]:
#                 smallest_range = (min_val, max_val)
                
#             if num_index+1 == len(nums[list_index]):
#                 return smallest_range
            
#             next_val = nums[list_index][num_index+1]
#             max_val = max(max_val, next_val)
#             heapq.heappush(min_heap, (next_val, list_index, num_index+1))
#         return smallest_range
        