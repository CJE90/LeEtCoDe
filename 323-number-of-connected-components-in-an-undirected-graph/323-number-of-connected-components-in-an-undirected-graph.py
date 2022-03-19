class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        count = 0
        visited = set()
        
        def explore(node):
            if node in visited:
                return
            visited.add(node)
            for child in adjList[node]:
                explore(child)
            return
        
        for i in range(n):
            if i not in visited:
                explore(i)
                count += 1
        return count