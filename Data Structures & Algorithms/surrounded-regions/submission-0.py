class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])
        dir=(-1,0,1,0)

        def dfs(i,j):
            if not (-1<i<m and -1<j<n and board[i][j]=='O'):
                return
            board[i][j]='#'
            for k in range(4):dfs(i+dir[k],j+dir[3-k])

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='#':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        
        