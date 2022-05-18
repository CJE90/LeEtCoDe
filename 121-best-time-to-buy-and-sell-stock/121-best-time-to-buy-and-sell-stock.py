class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxFound = 0
        minFound = inf
        for i in range(len(prices)-1):
            minFound = min(minFound, prices[i])
            if prices[i+1]>minFound:
                maxFound = max(maxFound, prices[i+1]-minFound)
        return maxFound
        