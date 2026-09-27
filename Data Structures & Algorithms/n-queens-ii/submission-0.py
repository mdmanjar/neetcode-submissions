class Solution:
    def totalNQueens(self, n: int) -> int:
        col=[False]*n
        d1=[False]*(n+n)
        d2=[False]*(n+n)
        ans=0
        def dfs(r):
            nonlocal ans
            if r==n:
                ans+=1
                return
            for c in range(n):
                if not col[c] and not d1[r+c] and not d2[n+r-c]:
                    col[c]=d1[r+c]=d2[n+r-c]=True
                    dfs(r+1)
                    col[c]=d1[r+c]=d2[n+r-c]=False
        dfs(0)
        return ans


        