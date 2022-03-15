class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        result = []
        
        def backtrack(index, dots, path):
            if dots == 4 and index == len(s):
                result.append(path[:-1])
                return
            if dots >= 4 or index > len(s):
                return
            
            for j in range(index, min(index+3, len(s))):
                segment = s[index:j+1]
                digit = int(segment)
                if digit > 255 or (len(segment) > 1 and segment[0] == '0'):
                    return
                backtrack(j+1, dots+1, path+segment+'.')
        backtrack(0,0,"")
        return result
            
        
       