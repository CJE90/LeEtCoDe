class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longestFound = 0
        count = defaultdict(int)
        
        for r in range(len(s)):
            
            count[s[r]]+=1
            largestCount = findMax(count)
            while (r-l+1) - largestCount > k:
                count[s[l]] -= 1
                if count[s[l]]<1:
                    count.pop(s[l])
                l+=1
            longestFound = max(longestFound, r-l+1)
        return longestFound
    
def findMax(listOfVal) -> int:
    largestFound = 0
    for val in listOfVal.values():
        largestFound = max(largestFound, val)
    return largestFound
        
            
            
    
                            
                
            