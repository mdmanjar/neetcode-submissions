from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2!=0:return False

        @lru_cache(None)
        def dfs(i,target):
            if target==0:return True
            if i==len(nums) or target<0:return False

            return dfs(i+1,target-nums[i]) or dfs(i+1,target)

        return dfs(0,sm//2)
        