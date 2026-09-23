class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid=[['.']*n for _ in range(n)]
        d1=[False]*(n+n)
        d2=[False]*(n+n)
        col=[False]*n
        ans=[]

        def dfs(i):
            if i==n:
                ans.append([''.join(row) for row in grid])
                return
            for j in range(n):
                if not col[j] and not d1[i+j] and not d2[n+i-j]:
                    col[j]=d1[i+j]=d2[n+i-j]=True
                    grid[i][j]='Q'
                    dfs(i+1)
                    col[j]=d1[i+j]=d2[n+i-j]=False
                    grid[i][j]='.'
        dfs(0)
        return ans
            

        