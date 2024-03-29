class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                circular_difference = ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            lookup[key].append(s)
        return lookup.values()
            