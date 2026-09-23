
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo=[None]*len(cost)
        def dfs(i):
            if i>=len(cost):return 0
            if memo[i] is not None:
                return memo[i]
            ans=cost[i]+min(dfs(i+2),dfs(i+1))
            memo[i]=ans
            return ans
        return min(dfs(0),dfs(1))
