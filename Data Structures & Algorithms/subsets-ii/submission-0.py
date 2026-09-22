class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        nums.sort()

        def dfs(i):
            ans.append(temp[:])
            st=set()
            for j in range(i,len(nums)):
                if nums[j] not in st:
                    st.add(nums[j])
                    temp.append(nums[j])
                    dfs(j+1)
                    temp.pop()
        dfs(0)
        return ans
                
        