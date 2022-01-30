class Solution:
    def minSwaps(self, data: List[int]) -> int:
        zeroCount = 0
        oneCount = 0
        for n in data:
            if n == 0:
                zeroCount += 1
            else:
                oneCount +=1
        print(zeroCount,oneCount)
        l = 0
        ans = len(data)
        count = 0
        
        for r in range(len(data)):
            if data[r] == 1:
                count +=1
            while r-l+1 == oneCount:
                if oneCount - count == (r-l+1)- count:
                    ans = min(ans, r-l+1-count)
                
                # if count == oneCount - ((r-l+1)-count):
                #     ans = min(ans, count)
                if data[l] == 1:
                    count -= 1
                l+=1
        return 0 if ans == len(data) else ans
            
        