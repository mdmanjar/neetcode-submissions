class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        n=len(nums)

        ans=[0]*n

        for i in range(n):
            ans[i]=left
            left*=nums[i]
        right=1

        for i in range(n-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        return ans
        