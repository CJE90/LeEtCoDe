class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        '''
        cba 1
        cba -> bac -> acb
        
        baaca 3
        baaca -> aacab -> aaabc
        '''        
        if k > 1:
            return ''.join(sorted(s))
        else:            
            return min(s[i:]+s[:i] for i in range(len(s)))
        
        
        
        
        