class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root={}

        def add(word):
            t=root
            for c in word:t=t.setdefault(c,{})
            t['#']=word
        for word in wordDict:
            add(word)
        ans=[]
        temp=[]

        def dfs(i):
            if i==len(s):
                ans.append(' '.join(temp))
                return 
            t=root
            for j,c in enumerate(s[i:],start=i):
                if c not in t:break
                t=t[c]
                if '#' in t:
                    temp.append(t['#'])
                    dfs(j+1)
                    temp.pop()
        dfs(0)
        return ans
    

