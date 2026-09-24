ans=[[1],[1,1]]
for i in range(2,34):
    ans.append([1]*(i+1))
    for j in range(1,i):
        ans[i][j]=ans[i-1][j-1]+ans[i-1][j]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return ans[rowIndex]

        