class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        dir=(-1,0,1,0)

        def dfs(i,j):
            if not (-1<i<m and -1<j<n and grid[i][j]=='1'):
                return
            grid[i][j]='0'
            for k in range(4):dfs(i+dir[k],j+dir[3-k])
        
        ans=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans


        