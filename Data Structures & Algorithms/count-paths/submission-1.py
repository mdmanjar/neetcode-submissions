class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n

        for i in range(1,m):
            # t=[1]*n

            for j in range(1,n):
                # t[j]=t[j-1]+dp[j]
                dp[j]=dp[j-1]+dp[j]


            # dp=t

        return dp[-1]