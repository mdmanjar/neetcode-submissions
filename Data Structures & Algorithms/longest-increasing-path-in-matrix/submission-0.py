class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[None]*n for _ in range(m)]
        dir=(-1,0,1,0)

        def dfs(i,j):
            if dp[i][j] is not None:
                return dp[i][j]
            ans=0
            for k in range(4):
                u=i+dir[k]
                v=j+dir[3-k]
                if -1<u<m and -1<v<n and grid[i][j]<grid[u][v]:
                    ans=max(dfs(u,v),ans)
            dp[i][j]=ans+1
            return dp[i][j]
        
        return max(dfs(i,j) for i in range(m) for j in range(n))
            

        