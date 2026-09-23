from math import inf
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:return 0

        @lru_cache(None)
        def dfs(amount):
            if amount==0:return 0

            ans=inf

            for coin in coins:
                if coin<=amount:
                    ans=min(dfs(amount-coin),ans)
            if ans==inf:return inf
            return ans+1
        ans=dfs(amount)
        return -1 if ans==inf else ans

        