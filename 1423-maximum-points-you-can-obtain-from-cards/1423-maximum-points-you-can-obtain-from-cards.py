class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalPoints = sum(cardPoints)
        
        l = 0
        largestFound = 0
        runningSum = 0
        n = len(cardPoints)
        if k == n:
            return totalPoints
        
        for r in range(len(cardPoints)):
            runningSum += cardPoints[r]
            
            if r-l + 1 == n-k:
                largestFound = max(largestFound, totalPoints-runningSum)
                runningSum -= cardPoints[l]
                l += 1
                
            
        return largestFound
        
        
        
            
        