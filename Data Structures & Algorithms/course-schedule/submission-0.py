class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        g=[[] for _ in range(n)]
        deg=[0]*n

        for u,v in edges:
            g[v].append(u)
            deg[u]+=1
        q=deque(i for i in range(n) if deg[i]==0)

        while q:
            n-=1
            u=q.popleft()

            for v in g[u]:
                deg[v]-=1
                if deg[v]==0:q.append(v)
        return n==0
        