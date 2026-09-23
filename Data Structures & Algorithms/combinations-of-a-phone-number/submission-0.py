class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:return []
        arr=('','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz')
        ans=[]
        temp=[]

        def dfs(i):
            if i==len(digits):
                ans.append(''.join(temp))
                return
            for c in arr[ord(digits[i])-48]:
                temp.append(c)
                dfs(i+1)
                temp.pop()
        dfs(0)
        return ans
        