class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])

        q=deque((i,j,1) for i in range(m) for j in range(n) if grid[i][j]==0)
        dir=(-1,0,1,0)

        while q:
            i,j,d=q.popleft()
            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]

                if -1<u<m and -1<v<n and grid[u][v]==2147483647:
                    grid[u][v]=d
                    q.append((u,v,d+1))


        