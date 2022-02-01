class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        water = 0
        l = 0
        r = len(height)-1
        while l < r:
            minheight = min(height[l], height[r])
            lengthOfBox = r-l
            areaOfWater = minheight*lengthOfBox
            
            water = max(water, areaOfWater)
            if height[l] <= height[r]:
                l += 1
            else:
                r-=1
        return water
        