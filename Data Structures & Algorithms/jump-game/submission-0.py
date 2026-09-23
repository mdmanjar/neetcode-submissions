class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=length:
                length=i

        return length==0