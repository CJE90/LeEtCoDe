class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        l = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            while len(count) == 3:
                count[s[l]] -= 1
                if count[s[l]] < 1:
                    count.pop(s[l])
                l += 1
            res += l
        return res     