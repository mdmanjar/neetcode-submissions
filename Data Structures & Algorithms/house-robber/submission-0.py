class Solution:
    def rob(self, nums: List[int]) -> int:
        rob=0
        notrob=0

        for coin in nums:
            notrob,rob=rob,max(rob,notrob+coin)

        return rob
        