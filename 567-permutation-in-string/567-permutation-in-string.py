class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        match_chars = 0
        lookup = Counter(s1)
        for right in range(len(s2)):
            right_char = s2[right]
            if right_char in lookup:
                lookup[right_char] -= 1
                if lookup[right_char] == 0:
                    match_chars += 1
            if match_chars == len(lookup):
                return True
            if right >= len(s1)-1:
                left_char = s2[left]
                if left_char in lookup:
                    if lookup[left_char] == 0:
                        match_chars -= 1
                    lookup[left_char] += 1
                left += 1
        return False
        