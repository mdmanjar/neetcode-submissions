from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mp=defaultdict(list)

        for u,v in tickets:
            mp[u].append(v)
        for v in mp.values():
            heapq.heapify(v)

        def dfs(u):
            while mp[u]:
                dfs(heapq.heappop(mp[u]))
            ans.append(u)
        ans=[]
        dfs('JFK')
        ans.reverse()
        return ans
        