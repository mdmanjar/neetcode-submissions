from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)+1
        dp=[[0]*n for _ in range(n)]

        for i in range(1,n):
            for j in range(1,n):
                if s[i-1]==s[n-j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        
        