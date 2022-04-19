from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0: return False
        sortedList = SortedList()
        for i,n in enumerate(nums):
            if i > k:
                sortedList.remove(nums[i-k-1])
            pos1 = bisect_left(sortedList, n-t);
            pos2 = bisect_right(sortedList,n+t)
            if pos1 != pos2:
                return True
            sortedList.add(n)
        return False
            
        