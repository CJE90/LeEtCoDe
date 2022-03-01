class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = [(List[0], list_index, 0) for list_index,List in enumerate(nums)]
        max_val = max(l[0] for l in nums)
        heapq.heapify(min_heap)
        smallest_range = (-inf,inf)
        while min_heap:
            min_val, list_index, num_index = heapq.heappop(min_heap)
            if max_val-min_val<smallest_range[1] - smallest_range[0]:
                smallest_range = (min_val,max_val)
            if num_index+1 == len(nums[list_index]):
                return smallest_range
            next_val = nums[list_index][num_index+1]
            max_val = max(max_val, next_val)
            heapq.heappush(min_heap, (next_val, list_index, num_index+1))
        