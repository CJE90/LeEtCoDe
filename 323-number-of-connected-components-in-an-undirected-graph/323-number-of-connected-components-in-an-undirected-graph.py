class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adjList = defaultdict(list)
        for node1,node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in adjList[node]:
                dfs(child)
            return
        
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
    