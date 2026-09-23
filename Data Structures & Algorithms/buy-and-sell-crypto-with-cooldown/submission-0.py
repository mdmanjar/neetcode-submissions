from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dfs(i,state):
            if len(prices)==i:return 0
            if state==0:
                return max(dfs(i+1,1)-prices[i],dfs(i+1,0))
            elif state==1:
                return max(dfs(i+1,2)+prices[i],dfs(i+1,1))
            else:
                return dfs(i+1,0)
        return dfs(0,0)
        