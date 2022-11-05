class Solution:
    def longestPalindrome(self, words: List[str]) -> int:        
        '''
        need same character in string 'xx'
        or two strings of opposites 'xy' 'yx'                
        '''        
        lookup = defaultdict(int)
        unpaired = 0
        count = 0
        for w in words:
            if w == w[::-1]:
                if lookup[w] > 0:
                    unpaired -= 1
                    lookup[w] -= 1
                    count += 4
                else:
                    lookup[w] += 1
                    unpaired += 1
            else:
                if lookup[w[::-1]] > 0:
                    lookup[w[::-1]] -= 1
                    count +=4
                else:
                    lookup[w] += 1
        if unpaired > 0:
            count += 2
        return count
    
   
        