class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mp=[None]*26

        for word in wordDict:
            i=ord(word[0])-97
            mp[i]=(word,mp[i])
        
        ans=[]
        temp=[]

        def dfs(i):
            if i==len(s):
                ans.append(' '.join(temp))
                return
            node=mp[ord(s[i])-97]
            while node:
                word,next=node
                if s.startswith(word,i):
                    temp.append(word)
                    dfs(i+len(word))
                    temp.pop()
                node=next
        dfs(0)
        return ans
        