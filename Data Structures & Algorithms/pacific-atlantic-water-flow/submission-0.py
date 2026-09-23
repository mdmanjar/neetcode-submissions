class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:

        dir=[-1,0,1,0]
        ans=[]
        m=len(h)
        n=len(h[0])

        vis=[[None]*n for _ in range(m)]

        def dfs(i,j,ocean):

            if vis[i][j]=='P' and ocean =='A':
                ans.append([i,j])


            vis[i][j]=ocean

            for k in range(4):

                u=i+dir[k]
                v=j+dir[3-k]

                if 0<=u<m and 0<=v<n and vis[u][v]!=ocean and h[u][v]>=h[i][j]:

                    dfs(u,v,ocean)


        for i in range(m):
          dfs(i,0,'P')


        for i in range(n):
          dfs(0,i,'P')

        for i in range(m):
          dfs(i,n-1,'A')

        for i in range(n):
          dfs(m-1,i,'A')

        return ans