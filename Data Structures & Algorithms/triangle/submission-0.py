class Solution:
    def minimumTotal(self, num: List[List[int]]) -> int:
        for i in range(len(num)-2,-1,-1):
            for j in range(len(num[i])):
                num[i][j]+=min(num[i+1][j],num[i+1][j+1])
        return num[0][0]

        