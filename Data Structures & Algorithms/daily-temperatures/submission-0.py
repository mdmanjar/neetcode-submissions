class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n
        stack=[]

        for i,e in enumerate(arr):
            while stack and arr[stack[-1]]<e:
                j=stack.pop()
                ans[j]=i-j
            stack.append(i)
        return ans
        