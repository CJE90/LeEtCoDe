class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        seen = set()
        que = deque()
        que.append([startGene, 0])
        seen.add(startGene)
        
        while que:
            node, steps = que.popleft()
            if node == endGene:
                return steps
            
            for c in 'ACTG':
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        que.append([neighbor, steps+1])
                        seen.add(neighbor)
        return -1
            
        