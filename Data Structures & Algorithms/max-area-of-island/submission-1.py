class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(i,j):
            if not (-1<i<m and -1<j<n and grid[i][j]):return 0
            grid[i][j]=0
            ans=1
            for k in range(4):
                ans+=dfs(i+dir[k],j+dir[3-k])
            return ans
            
        
        dir=(-1,0,1,0)

        return max(dfs(i,j) for i in range(m) for j in range(n))

        