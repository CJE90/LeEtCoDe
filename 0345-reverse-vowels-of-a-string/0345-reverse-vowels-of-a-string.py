class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        S = list(s)
        left = 0
        right = len(s)-1
        while left<right:
            while left < len(s) and S[left].lower() not in vowels:
                left +=1
            while right >= 0 and S[right].lower() not in vowels:
                right -= 1
            if left < right:
                S[left], S[right] = S[right], S[left]
                left +=1
                right -= 1
        return "".join(S)
        