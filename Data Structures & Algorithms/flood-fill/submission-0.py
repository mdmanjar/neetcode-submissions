class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc]==color:return image
        m,n=len(image),len(image[0])
        already_color=image[sr][sc]

        def dfs(i,j):
            if not (-1<i<m and -1<j<n and image[i][j]==already_color):
                return 
            image[i][j]=color
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
        
        dfs(sr,sc)
        return image
        