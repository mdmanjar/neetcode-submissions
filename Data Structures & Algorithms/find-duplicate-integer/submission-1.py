class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            v=abs(nums[i])-1
            if nums[v]<0:return abs(nums[i])
            nums[v]=-abs(nums[v])

        