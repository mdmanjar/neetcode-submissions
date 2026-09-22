class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        buy=math.inf
        for e in prices:
            buy=min(e,buy)
            ans=max(ans,e-buy)
        return ans
        