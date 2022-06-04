class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        minLength = inf
        for word in strs:
            minLength = min(minLength, len(word))
        for i in range(minLength):
            c = strs[0][i]
            same = True
            for word in strs:
                if word[i] != c:
                    same = False
            if same:
                answer.append(c)
            else:
                return "".join(answer)
        return "".join(answer)
        