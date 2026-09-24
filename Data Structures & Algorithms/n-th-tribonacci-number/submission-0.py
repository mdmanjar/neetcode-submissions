class Solution:
    def tribonacci(self, n: int) -> int:
        from functools import cache
        @cache
        def dfs(n):
            if n<=1:return n
            if n==2:return 1
            return dfs(n-1)+dfs(n-2)+dfs(n-3)
        return dfs(n)
        