class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
            arrows = len(points)
            points.sort(key = lambda x:x[1])
            prevEnd = -inf
            for balloon in points:
                if balloon[0] > prevEnd:
                    prevEnd = balloon[1]
                else:
                    arrows-=1
                    #prevEnd = min(prevEnd, balloon[1])
            return arrows
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         needed_arrrows = len(points)
#         points.sort(key = lambda x:x[1])
#         prev_ballon_end = -inf
#         for s,e in points:
#             if s > prev_ballon_end:
#                 prev_ballon_end = e
#             else:
#                 needed_arrrows -= 1
#         return needed_arrrows
    
    
    
    
    
    
    