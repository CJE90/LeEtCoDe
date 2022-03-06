class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = set()
        adjList = defaultdict(list)
        que = deque()
        steps = 0
        
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjList[pattern].append(word)
        print(adjList)
        que.append(beginWord)
        visited.add(beginWord)
        
        while que:
            n = len(que)
            steps+=1
            for _ in range(n):
                curWord = que.popleft()
                if curWord == endWord:
                    return steps
                for i in range(len(curWord)):
                    pattern = curWord[:i] + '*' + curWord[i+1:]
                    for w in adjList[pattern]:
                        if w not in visited:
                            que.append(w)
                            visited.add(w)           
        return 0
              
