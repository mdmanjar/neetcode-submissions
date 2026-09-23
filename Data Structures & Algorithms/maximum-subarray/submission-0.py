class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-math.inf
        sum=0

        for e in nums:
            sum+=e
            ans=max(sum,ans)
            sum=max(sum,0)
        return ans
        