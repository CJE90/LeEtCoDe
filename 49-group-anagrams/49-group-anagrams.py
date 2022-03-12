class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for word in strs:
            lookup[tuple(sorted(word))].append(word)
        
        return lookup.values()