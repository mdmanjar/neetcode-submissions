class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root={}

        def add(word):
            t=root

            for c in word:t=t.setdefault(c,{})
            t['#']=word
        
        for word in words:add(word)

        dir=(-1,0,1,0)

        ans=[]

        def dfs(i,j,root):
            if '#' in root:
                ans.append(root['#'])
                del root['#']
            prev=board[i][j]
            board[i][j]='#'
            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]
                if -1<u<m and -1<v<n and board[u][v] in root:
                    dfs(u,v,root[board[u][v]])
            board[i][j]=prev
        m,n=len(board),len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i,j,root[board[i][j]])
        return ans
            

        