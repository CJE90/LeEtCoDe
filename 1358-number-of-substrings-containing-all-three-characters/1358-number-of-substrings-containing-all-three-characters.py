class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        startWindow = 0
        count = 0 
        d = {'a':0,'b':0,'c':0}

        for endWindow in range(len(s)):
            d[s[endWindow]]+=1

            while  all(d.values()):
                count += len(s)-endWindow
                d[s[startWindow]] -= 1
                startWindow += 1
      
        return count
            
        
        
        