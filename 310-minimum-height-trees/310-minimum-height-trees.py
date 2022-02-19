class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        # print(adjList)
        # neighbors = [set() for i in range(n)]
        # for node1, node2 in edges:
        #     neighbors[node1].add(node2)
        #     neighbors[node2].add(node1)
        # print(neighbors)
        
        leaves = []
        for i in range(n):
            if len(adjList[i]) == 1:
                leaves.append(i)
                
        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = adjList[leaf].pop()
                adjList[neighbor].remove(leaf)
                if len(adjList[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves
            