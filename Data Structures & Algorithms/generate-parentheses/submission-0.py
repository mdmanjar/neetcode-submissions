class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        temp=[]

        def dfs(open,close):
            if close==n:
                ans.append(''.join(temp))
                return

            if open<n:
                temp.append('(')
                dfs(open+1,close)
                temp.pop()

            if close<open:
                temp.append(')')
                dfs(open,close+1)
                temp.pop()

        dfs(0,0)
        return ans
        