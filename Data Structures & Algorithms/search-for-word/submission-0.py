class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir=(-1,0,1,0)
        m,n=len(board),len(board[0])

        def dfs(i,j,k):
            if k==len(word):return True
            if not (-1<i<m and -1<j<n and word[k]==board[i][j]):
                return False
            x=board[i][j]
            board[i][j]='#'
            ans=any(dfs(i+dir[d],j+dir[3-d],k+1) for d in range(4))
            board[i][j]=x
            return ans
        
        return any(dfs(i,j,0) for i in range(m) for j in range(n))
        