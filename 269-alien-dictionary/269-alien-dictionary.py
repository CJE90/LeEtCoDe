class Solution:
    def alienOrder(self, words: List[str]) -> str:
        result = []
        adjList = defaultdict(set)
        inDegree = {c:0 for w in words for c in w}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) > len(word2) and word2 == word1[: len(word2)]:
                    return ""
            for j in range(len(word1)):
                
                if word1[j] == word2[j]:
                    continue
                if word2[j] not in adjList[word1[j]]:
                    inDegree[word2[j]] += 1
                adjList[word1[j]].add(word2[j])
                break
                    
        que = deque()
        for c in inDegree:
            if inDegree[c] == 0:
                que.append(c)
        while que:
            char = que.popleft()
            result.append(char)
            for l in adjList[char]:
                inDegree[l] -= 1
                if inDegree[l] == 0:
                    que.append(l)
        res = "".join(result)
        if len(res) == len(inDegree):
            return res
        return ""

