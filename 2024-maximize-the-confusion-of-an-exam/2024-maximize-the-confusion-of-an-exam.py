class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        longestFound = 0
        count = defaultdict(int)
        maxf = 0
        
        for r in range(len(answerKey)):
            count[answerKey[r]]+=1
            if count[answerKey[r]] > maxf:
                maxf = count[answerKey[r]]
            while (r-l+1) - maxf > k:
                count[answerKey[l]] -= 1
                l+=1
            longestFound = max(longestFound, r-l+1)
        return longestFound
            