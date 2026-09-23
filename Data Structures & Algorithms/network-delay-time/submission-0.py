class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        g=[[] for _ in range(n)]

        for u,v,w in times:
            g[u-1].append((v-1,w))

        dist=[math.inf]*n

        dist[k-1]=0
        hp=[(0,k-1)]

        while hp:
            d,u=heapq.heappop(hp)

            if d>dist[u]:continue

            for v , w, in g[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(hp,(nd,v))

        ans=max(dist)
        return ans if ans!=math.inf else -1
        