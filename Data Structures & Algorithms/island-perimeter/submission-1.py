class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dir=(-1,0,1,0)
        def dfs(i,j):
            if not (-1<i<m and -1<j<n):return 1
            if grid[i][j]==0:return 1
            if grid[i][j]==-1:return 0
            ans=0
            grid[i][j]=-1
            return sum(dfs(i+dir[k],j+dir[3-k]) for k in range(4))
        
        return sum(dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]==1)
        