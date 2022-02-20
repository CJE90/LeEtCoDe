class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjList = defaultdict(list)
        # signalReceivedAt = [inf for i in range(len(times))]
        # t={}
        # for v1, v2, w in times:
        #     adjList[v1].append((v2, w))
        # minHeap = [(k, 0)]
        # while minHeap:
        #     node, time = heapq.heappop(minHeap)
        #     if node not in t:
        #         t[node] = time
        #         for adjNode, newTime in adjList[node]:
        #             heapq.heappush(minHeap, (adjNode, time+newTime))
        # return max(t.values()) if len(t) == n else -1
        q, t, adj = [(0, k)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == n else -1
        
        
        
        '''
        class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1
        '''
        
        