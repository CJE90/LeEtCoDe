class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def possible(capacity) -> bool:
            curDays = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    curDays += 1
                    if curDays > days:  # cannot ship within D days
                        return False
            return True
        
        while left < right:
            mid = left + (right-left) // 2
            
            if possible(mid):
                right = mid
            else:
                left = mid+1
        return left