class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dir=(-1,0,1,0)
        fresh_orange=0
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh_orange+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        if fresh_orange==0:return 0
        if not q:return -1

        minute=0

        while q and fresh_orange:
            for _ in range(len(q)):
                i,j=q.popleft()

                for k in range(4):
                    u,v=i+dir[k],j+dir[3-k]
                    if -1<u<m and -1<v<n and grid[u][v]==1:
                        grid[u][v]=2
                        q.append((u,v))
                        fresh_orange-=1

            minute+=1
        return minute if fresh_orange==0 else -1


        