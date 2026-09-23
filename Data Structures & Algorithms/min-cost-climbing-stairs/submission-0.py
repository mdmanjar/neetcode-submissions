from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @lru_cache(None)
        def dfs(i):
            if i>=len(cost):return 0
            ans=cost[i]+min(dfs(i+2),dfs(i+1))
            return ans
        return min(dfs(0),dfs(1))
