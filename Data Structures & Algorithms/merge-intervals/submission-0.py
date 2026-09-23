class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort(key=lambda x:x[0])

        ans=[]

        for x in arr:
            if not ans or ans[-1][1]<x[0]:
                ans.append(x)
            else:
                ans[-1][0]=min(ans[-1][0],x[0])
                ans[-1][1]=max(ans[-1][1],x[1])
        return ans

        