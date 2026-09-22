class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]

        def dfs(sm,i):
            if sm==0:
                ans.append(temp[:])
            if sm<=0 or i==len(nums):return
            temp.append(nums[i])
            dfs(sm-nums[i],i)
            temp.pop()
            dfs(sm,i+1)
        dfs(target,0)
        return ans

        
        