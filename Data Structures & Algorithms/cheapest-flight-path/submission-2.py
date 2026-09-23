class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g=[[]  for _ in range(n)]
        

        for u,v ,p in flights:
            g[u].append((v,p))

        stops=[math.inf]*n

        hp=[(0,0,src)]

        while hp:
            d,stop,u=heapq.heappop(hp)
            if u==dst:
                return d
            if stop>k:
                continue
            if stop>=stops[u]:
                continue
            stops[u]=stop
            for v,p in g[u]:
                heapq.heappush(hp,(p+d,stop+1,v))
        return -1
            