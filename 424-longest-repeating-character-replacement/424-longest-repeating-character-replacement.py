class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = defaultdict(int)
        l = 0
        maxLength = 0
        mostFrequent = ''
        for r in range(len(s)):
            lookup[s[r]] += 1
            mostFrequent = max(lookup.values())
            while r-l+1-mostFrequent > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] < 1:
                    lookup.pop(s[l])
                l +=1
            maxLength = max(maxLength, r-l+1)
        return maxLength
        