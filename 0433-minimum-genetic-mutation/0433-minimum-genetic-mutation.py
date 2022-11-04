class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        seen = set(start)
        que = deque()
        que.append([start,0])
        
        while que:
            node, steps = que.popleft()
            if node == end:
                return steps
                        
            for c in 'ACTG':
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        que.append([neighbor, steps+1])
                        seen.add(neighbor)
                        
        return -1
