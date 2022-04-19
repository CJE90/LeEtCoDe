class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for word in strs:
            sortedWord = sorted(word)
            lookup[tuple(sortedWord)].append(word)
        return lookup.values()
            
                
        