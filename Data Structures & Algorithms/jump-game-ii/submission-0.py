class Solution:
    def jump(self, nums: List[int]) -> int:
        length=len(nums)
        jump=0
        currMax=0
        currEnd=0

        for i in range(length-1):
            currMax=max(currMax,i+nums[i])

            if i==currEnd:
                jump+=1
                currEnd=currMax

        return jump