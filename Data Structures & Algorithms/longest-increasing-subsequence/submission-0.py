from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[]

        for e in nums:
            idx=bisect_left(arr,e)
            if idx==len(arr):
                arr.append(e)
            else:
                arr[idx]=e
        return len(arr)
        