class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(i,j):
            while i<j:
                if s[i]!=s[j]:return False
                i+=1
                j-=1
            return True
        ans=[]
        temp=[]

        def dfs(i):
            if i==len(s):
                ans.append(temp[:])
                return

            for j in range(i,len(s)):
                if check(i,j):
                    temp.append(s[i:j+1])
                    dfs(j+1)
                    temp.pop()
        dfs(0)
        return ans

        