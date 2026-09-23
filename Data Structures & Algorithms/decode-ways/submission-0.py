from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache
        def dfs(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            ans=dfs(i+1)
            if i+1<len(s):
                x=int(s[i:i+2])
                if 10<=x<=26:
                    ans+=dfs(i+2)
            return ans
        return dfs(0)
        