class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        hp=[(grid[0][0],0,0)]
        m,n=len(grid),len(grid[0])
        dir=(-1,0,1,0)
        grid[0][0]=-1
        ans=0

        while hp:
            d,i,j=heapq.heappop(hp)
            ans=max(ans,d)

            if (i,j)==(m-1,n-1):return ans

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]
                if -1<u<m and -1<v<n and grid[u][v]!=-1:
                    heapq.heappush(hp,(grid[u][v],u,v))
                    grid[u][v]=-1
        return ans
        