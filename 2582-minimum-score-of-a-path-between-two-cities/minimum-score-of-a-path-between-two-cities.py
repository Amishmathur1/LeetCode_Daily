class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u,v,w in roads:
            adj[v].append((u,w))
            adj[u].append((v,w))
        
        vis = [False] * (n+1)
        dq = deque([1])
        vis[1] = True
    
        ans = float('inf')
        while dq:
            node = dq.popleft()
            for nei, wei in adj[node]:

                ans = min(ans, wei)

                if not vis[nei]:
                    vis[nei] = True
                    dq.append(nei)
        
        return ans