class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        return max(self._rob(nums[:n-1]),self._rob(nums[1:]))

    def _rob(self, nums: List[int]) -> int:
        rob=0
        notrob=0

        for coin in nums:
            notrob,rob=rob,max(rob,notrob+coin)

        return rob
        