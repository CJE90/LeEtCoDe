class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_window = 0
        max_char = 0
        lookup = defaultdict(int)
        for right in range(len(s)):
            lookup[s[right]] += 1
            max_char = max(max_char, lookup[s[right]])
            if (right-left+1 - max_char) > k:
                lookup[s[left]] -= 1
                if lookup[s[left]] < 1:
                    del lookup[s[left]]
                left += 1
            max_window = max(max_window, right-left+1)
        return max_window
        