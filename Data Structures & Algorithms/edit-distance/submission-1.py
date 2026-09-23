
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)<len(word2):
            word1,word2=word2,word1
        m=len(word1)
        n=len(word2)
        dp=list(range(n+1))
        for i in range(1,m+1):
            t=[i]+[0]*n
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    t[j]=dp[j-1]
                else:
                    t[j]=min(t[j-1],dp[j-1],dp[j])+1
            dp=t
        return dp[-1]


