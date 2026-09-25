class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:return 0
        m,n=len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j]=None
        for i in range(m):
            for j in range(n):
                if grid[i][j] is None:continue
                if i==0 and j==0:grid[i][j]=1
                elif i==0 and grid[i][j-1] is not None:
                    grid[i][j]+=grid[i][j-1]
                elif j==0 and grid[i-1][j] is not None:
                    grid[i][j]+=grid[i-1][j]
                else:
                    if grid[i-1][j]:
                        grid[i][j]+=grid[i-1][j]
                    if grid[i][j-1]:
                        grid[i][j]+=grid[i][j-1]

        return grid[-1][-1]

        