class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        l = 0
        maxWindow = 0
        for r in range(len(s)):
            while s[r] in lookup:
                lookup.remove(s[l])
                l += 1
            lookup.add(s[r])
            maxWindow = max(r-l+1, maxWindow)
        return maxWindow
        