class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        lookup = Counter(s1)
        need_to_match = 0        
        for right in range(len(s2)):
            if s2[right] in lookup:
                lookup[s2[right]] -= 1
                if lookup[s2[right]] == 0:
                    need_to_match += 1
            if need_to_match == len(lookup):
                return True
            if right >= len(s1)-1:
                if s2[left] in lookup:                    
                    if lookup[s2[left]] == 0:
                        need_to_match -= 1
                    lookup[s2[left]] += 1
                left += 1
        return False