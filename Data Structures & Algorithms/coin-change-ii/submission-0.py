from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @ lru_cache(None)
        def dfs(i,amount):
            if amount==0:return 1
            if amount<0 or i==len(coins):
                return 0
            return dfs(i,amount-coins[i])+dfs(i+1,amount)
        return dfs(0,amount)

        