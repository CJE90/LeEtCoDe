class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord) or endWord not in wordList:
            return 0
        adjList = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for c in range(len(word)):
                pattern = word[:c] + '*' + word[c+1:]
                adjList[pattern].append(word)
        print(adjList)
        visited = set([beginWord])
        que = deque([beginWord])
        que.append(beginWord)
        level = 1
        
        while que:
            
            for i in range(len(que)):
                word = que.popleft()
                if word == endWord:
                    return level
                
                for j in range(len(word)):
                    pattern = word[:j] +'*' + word[j+1:]
                    for w in adjList[pattern]:
                        if w not in visited:
                            que.append(w)
                            visited.add(w)
                    
            
            level += 1
            
            
        return 0
            
            
            
        
        