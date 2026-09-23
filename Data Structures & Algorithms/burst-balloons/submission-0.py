from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]

        @lru_cache(None)
        def dfs(left,right):
            if left>right:
                return 0

            ans=0

            for i in range(left,right+1):
                x=nums[left-1]*nums[i]*nums[right+1]
                ans=max(ans,dfs(left,i-1)+x+dfs(i+1,right))

            return ans

        return dfs(1,len(nums)-2)