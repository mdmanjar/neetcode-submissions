class Solution:
    def insert(self, num: List[List[int]], x: List[int]) -> List[List[int]]:
        ans=[]
        i=0

        while i<len(num) and num[i][1]<x[0]:
            ans.append(num[i])
            i+=1

        while i<len(num) and num[i][0]<=x[1]:
            x[0]=min(x[0],num[i][0])
            x[1]=max(x[1],num[i][1])
            i+=1

        ans.append(x)

        while i<len(num):
            ans.append(num[i])
            i+=1

        return ans