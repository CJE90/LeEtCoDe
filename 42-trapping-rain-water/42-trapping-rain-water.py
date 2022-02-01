class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left = max_right = tmp = 0
        # for i in range(len(height)):
        #     max_left = max(height[i], max_left)
        #     max_right = max(height[-1-i], max_right)
        #     tmp += max_left + max_right - height[i]
        # result = tmp - len(height) * max_left
        # return result

        leftStack = []
        maxleft = 0
        maxright = 0
        rightStack = []
        mins = []
        tw = 0
        
        for i in range(len(height)):
            leftStack.append(maxleft)
            maxleft = max(maxleft, height[i])
        for j in range(len(height)-1,-1,-1):
            rightStack.append(maxright)
            maxright = max(maxright, height[j])
        rightStack.reverse()
        
        for i in range(len(height)):
            mins.append(min(leftStack[i], rightStack[i]))
        
        for i in range(len(height)):
            if mins[i] - height[i] >= 0:
                tw += mins[i] - height[i]
        return tw
                
            
        
        