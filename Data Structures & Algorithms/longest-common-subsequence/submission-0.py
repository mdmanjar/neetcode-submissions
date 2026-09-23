class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1==text2:return len(text1)
        if len(text1)<len(text2):
            text1,text2=text2,text1
        m,n=len(text1),len(text2)
        dp=[0]*(n+1)

        for i in range(1,m+1):
            t=[0]*(n+1)
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    t[j]=dp[j-1]+1
                else:
                    t[j]=max(t[j-1],dp[j])
            dp=t
        return dp[-1]
        