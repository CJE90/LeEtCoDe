class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adjList = defaultdict(list)
        for node1,node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        que = deque()
        
        def bfs(node):
            que.append(node)
            while que:
                curNode = que.popleft()
                visited.add(curNode)
                for child in adjList[curNode]:
                    if child not in visited:
                        que.append(child)
        
                    
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        return count
        
    