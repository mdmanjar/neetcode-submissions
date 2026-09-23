class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=-math.inf
        p=1
        for  e in nums:
            p*=e
            ans=max(p,ans)
            if p==0:p=1
        p=1

        for e in nums[::-1]:
            p*=e
            ans=max(ans,p)
            if p==0:p=1
        return ans
        