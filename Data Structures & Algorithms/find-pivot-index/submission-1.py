class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm=sum(nums)
        prev=0
        for i,e in enumerate(nums):
            if prev==(sm-prev-e):return i
            prev+=e
        return -1
        