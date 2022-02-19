class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        result = []
       
        stack = [(0,[0])]

        while stack:
            node, path = stack.pop()
            if node == target:
                result.append(path)
            for nbor in graph[node]:
                stack.append((nbor, path+[nbor]))
        return result