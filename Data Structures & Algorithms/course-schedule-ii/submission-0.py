class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n)]
        deg=[0]*n

        for u,v in edges:
            g[v].append(u)
            deg[u]+=1
        q=deque(i for i in range(n) if deg[i]==0)

        ans=[]

        while q:
            n-=1
            u=q.popleft()
            ans.append(u)

            for v in g[u]:
                deg[v]-=1
                if deg[v]==0:q.append(v)
        if n:return []
        return ans
        