class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        lookup = Counter(secret)
        bull = 0
        cow = 0
        
        for index,char in enumerate(guess):
            if secret[index]==guess[index]:
                bull += 1
                if lookup[char]<=0:
                    cow-=1
                    
                
            else:
                if char in lookup and lookup[char] > 0:
                    cow +=1
            lookup[char] -= 1
                
        return str(bull)+'A'+str(cow)+'B'
            
        