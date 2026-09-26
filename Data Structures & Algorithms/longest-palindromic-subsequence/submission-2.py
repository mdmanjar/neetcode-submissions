from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)+1
        dp=[0]*n

        for i in range(1,n):
            t=[0]*n
            for j in range(1,n):
                if s[i-1]==s[n-j-1]:
                    t[j]=dp[j-1]+1
                else:
                    t[j]=max(t[j-1],dp[j])
            dp=t
        return dp[-1]
        
        