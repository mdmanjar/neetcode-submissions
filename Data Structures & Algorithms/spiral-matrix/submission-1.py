class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        dir=((0,1),(1,0),(0,-1),(-1,0))

        def next(i,j,d):
            x,y=dir[d]
            i=x+i
            j=y+j
            if -1<i<m and -1<j<n and grid[i][j] is not None:
                return d
            return (d+1)%4
        i=j=d=0
        ans=[]
        m,n=len(grid),len(grid[0])
        total=m*n

        while total:
            ans.append(grid[i][j])
            grid[i][j]=None
            d=next(i,j,d)
            x,y=dir[d]
            i+=x
            j+=y
            total-=1
        return ans


        