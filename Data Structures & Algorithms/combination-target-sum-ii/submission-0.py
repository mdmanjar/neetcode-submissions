class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        nums.sort()

        def dfs(sm,i):
            if sm==0:
                ans.append(temp[:])
            if sm<=0 or i==len(nums):
                return
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                temp.append(nums[j])
                dfs(sm-nums[j],j+1)
                temp.pop()
        dfs(target,0)
        return ans

        