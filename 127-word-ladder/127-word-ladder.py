class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjList = defaultdict(list)
        visited = set()
        que = deque()
        level = 0
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] +'*'+word[i+1:]
                adjList[pattern].append(word)
        
        que.append(beginWord)
        visited.add(beginWord)
        while que:
            level+=1
            n = len(que)
            for _ in range(n):
                curWord = que.popleft()
                if curWord == endWord:
                    return level
                
                for i in range(len(curWord)):
                    pattern = curWord[:i] +'*'+curWord[i+1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visited:
                            que.append(neighbor)
                            visited.add(neighbor)
            
        return 0
        
        