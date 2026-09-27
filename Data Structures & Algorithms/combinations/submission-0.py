class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        temp=[]

        def dfs(i):
            if len(temp)==k:
                ans.append(temp[:])
                return
            if i>n:return
            temp.append(i)
            dfs(i+1)
            temp.pop()
            dfs(i+1)
        dfs(1)
        return ans
        