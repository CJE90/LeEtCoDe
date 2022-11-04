class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        seen = set()
        queue = deque()
        # add our first node into the queue and add it to our seen set
        # seen will prevent us from visiting the same node twice
        queue.append([start,0])
        seen.add(start)
        
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps
            
            for c in 'ACGT':
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    #AACCGGTT
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps+1))
                        seen.add(neighbor)
        return -1
                    
        
        