class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        from functools import cache
        @cache
        def dfs(target):
            if target==0:return 1
            ans=0

            for e in nums:
                if e<=target:ans+=dfs(target-e)
                else:break
            return ans
        return dfs(target)
        