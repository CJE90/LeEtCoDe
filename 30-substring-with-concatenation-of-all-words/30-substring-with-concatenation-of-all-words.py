class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        allWords = Counter(words)
        wordLen = len(words[0])
        numWords = len(words)
        totalLength = numWords*wordLen
        result = []
        for i in range(len(s) - totalLength+1):
            seen = defaultdict(int)
            for j in range(i, i+totalLength, wordLen):
                curWord = s[j:j+wordLen]
                if curWord in allWords:
                    seen[curWord] += 1
                    if seen[curWord] > allWords[curWord]:
                        break
                else:
                    break
            if seen == allWords:
                result.append(i)
        return result
        
        
        
#         wordBag = Counter(words)   # count the freq of each word
#         wordLen, numWords = len(words[0]), len(words)
#         totalLen, res = wordLen*numWords, []
#         for i in range(len(s)-totalLen+1):   # scan through s
#             # For each i, determine if s[i:i+totalLen] is valid
#             seen = defaultdict(int)   # reset for each i
#             for j in range(i, i+totalLen, wordLen):
#                 currWord = s[j:j+wordLen]
#                 if currWord in wordBag:
#                     seen[currWord] += 1
#                     if seen[currWord] > wordBag[currWord]:
#                         break
#                 else:   # if not in wordBag
#                     break    
#             if seen == wordBag:
#                 res.append(i)   # store result
#         return res
        