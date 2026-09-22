class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[False]*9 for _ in range(9)]
        cols=[[False]*9 for _ in range(9)]
        box=[[False]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    idx=ord(board[i][j])-49
                    bid=(i//3)*3+(j//3)
                    if rows[i][idx] or cols[j][idx] or box[bid][idx]:return False
                    rows[i][idx]=True
                    cols[j][idx]=True
                    box[bid][idx]=True
        return True


        